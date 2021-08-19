(n, m, k) = map(int, input().split())
d = max(0, n // k - (n - m))
M = 1000000009
if d > 0:
    res = (2 * k * (pow(2, d, M) - 1) % M + m - k * d) % M
else:
    res = m
print(res)
