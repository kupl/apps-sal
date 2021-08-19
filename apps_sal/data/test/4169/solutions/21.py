(n, m) = list(map(int, input().split()))
stores = [list(map(int, input().split())) for _ in range(n)]
sorted_sotres = sorted(stores, key=lambda x: x[0])
total = 0
ans = 0
for (cost, number) in sorted_sotres:
    if number > m:
        ans += cost * m
        break
    elif number == m:
        ans += cost * number
        break
    else:
        ans += cost * number
    m -= number
print(ans)
