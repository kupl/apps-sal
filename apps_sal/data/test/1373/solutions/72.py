n, k = map(int, input().split())
d, u = 0, 10**1000
ans = 0
while d < u:
    d = (k * (k - 1)) // 2
    u = (2 * k * n - k**2 + k) // 2
    ans += u - d + 1
    k += 1
print(ans % (10**9 + 7))
