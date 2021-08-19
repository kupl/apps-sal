(L, R) = map(int, input().split())
ans = 2020
for i in range(L, R + 1):
    for j in range(i + 1, R + 1):
        n = i * j
        if n % 2019 == 0:
            ans = 0
            break
        n = n % 2019
        ans = min(ans, n)
    else:
        continue
    break
print(ans)
