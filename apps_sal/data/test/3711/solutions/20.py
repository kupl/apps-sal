n, m, k = list(map(int, input().split()))
ans, ans1 = 0, 0
if n + m - 2 < k:
    print(-1)
    return
else:
    k1 = k
    if k < n:
        ans = (n // (k + 1)) * m
    else:
        k -= (n - 1)
        ans = (m // (k + 1))
    if k1 < m:
        ans1 = (m // (k1 + 1)) * n
    else:
        k1 -= (m - 1)
        ans1 = (n // (k1 + 1))
print(max(ans1, ans))
