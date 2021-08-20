(n, m, k) = map(int, input().split())
if m > n:
    (n, m) = (m, n)
ans = -1
if k < n:
    ans = m * (n // (k + 1))
    if k < m:
        ans = max(ans, n * (m // (k + 1)))
elif k <= n - 1 + (m - 1):
    ans = m // (k + 1 - n + 1)
print(ans)
