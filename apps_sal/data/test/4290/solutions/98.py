(n, m) = list(map(int, input().split()))
ans = 0
if n >= 2:
    ans += n * (n - 1) // 2
if m >= 2:
    ans += m * (m - 1) // 2
print(ans)
