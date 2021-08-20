def c(n, k):
    if k > n:
        return 0
    a = b = 1
    for i in range(n - k + 1, n + 1):
        a *= i
    for i in range(1, k + 1):
        b *= i
    return a // b


(a, b, k, t) = map(int, input().split())
(n, m, s) = (2 * k + 1, 2 * t, 2 * k * t + b - a)
(ans, mod) = (0, 1000000007)
for i in range(m + 1):
    ans = (ans + [1, -1][i & 1] * c(m, i) * c(m + s - n * i, m)) % mod
print((pow(n, m, mod) - ans) % mod)
