(k, s) = map(int, input().split())
ans = 0
for i in range(k + 1):
    for j in range(k + 1):
        t = s - (i + j)
        if 0 <= t <= k:
            ans += 1
print(ans)
