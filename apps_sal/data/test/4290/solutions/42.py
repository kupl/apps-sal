n, m = map(int, input().split())
ans = 0
if n >= 2:
    ans += n * (n - 1) // 2
else:
    ans += 0

if m >= 2:
    ans += m * (m - 1) // 2
else:
    ans += 0

print(ans)
