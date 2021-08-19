(n, k) = map(int, input().split())
a = list(map(int, input().split()))
(ans, s) = (0, 0)
r = 0
for l in range(n):
    while r < n and s < k:
        s += a[r]
        r += 1
    if s >= k:
        ans += n - r + 1
    s -= a[l]
print(ans)
