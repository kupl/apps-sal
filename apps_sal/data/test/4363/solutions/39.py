(k, s) = list(map(int, input().split()))
ans = 0
for i in range(k + 1):
    for j in range(k + 1):
        m = s - i - j
        if 0 <= m <= k:
            ans += 1
print(ans)
