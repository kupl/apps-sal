n, k = list(map(int, input().split()))
g = [1] * k
mod = 10 ** 9 + 7

for i in range(k, 0, -1):
    x = k // i
    m = n
    while m > 0:
        if m & 1:
            g[i-1] = g[i-1] * x % mod
        x = x * x % mod
        m >>= 1

    y = 2
    while i * y <= k:
        g[i-1] -= g[i*y-1]
        y += 1

ans = 0
for i in range(k):
    ans = (ans + g[i] * (i + 1)) % mod

print(ans)

