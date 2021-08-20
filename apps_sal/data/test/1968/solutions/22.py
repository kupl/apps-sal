(n, v) = map(int, input().split())
sellers = [list(map(int, input().split())) for i in range(n)]
(res_amount, res_sellers) = (0, [])
for (i, p) in enumerate(sellers):
    if min(p[1:]) < v:
        res_amount += 1
        res_sellers.append(i + 1)
print(res_amount)
print(*res_sellers)
