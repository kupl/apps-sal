(n, m) = list(map(int, input().split()))
ans = 0
if n < m:
    if 2 * n <= m:
        m = m - 2 * n
        ans += n
    ans += m // 4
else:
    ans += m // 2
print(ans)
