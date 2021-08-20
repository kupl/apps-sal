(n, m) = list(map(int, input().strip().split()))
ab_list = [list(map(int, input().strip().split())) for _ in range(m)]
ab_list.sort(key=lambda x: x[1])
res = 0
min_r = 0
for ab in ab_list:
    if min_r <= ab[0]:
        res += 1
        min_r = ab[1]
print(res)
