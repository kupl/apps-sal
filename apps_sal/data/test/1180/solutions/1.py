n, k = list(map(int, input().split()))
t = list(map(int, input()))

s = 0

d = 10 ** 9 + 7
f = [1] * n

for i in range(2, n):
    f[i] = (i * f[i - 1]) % d


def c(a, b): return 0 if a > b else (f[b] * pow(f[a] * f[b - a], d - 2, d)) % d


if k:
    p = [1] * (n + 1)
    for i in range(n):
        p[i + 1] = (10 * p[i]) % d

    x = [p[i] * c(k - 1, n - 2 - i) for i in range(n + 1)]
    for i in range(n):
        x[i] = (x[i] + x[i - 1]) % d

    for i in range(n):
        y = x[n - 2 - i] + p[n - 1 - i] * c(k, i)
        s = (s + t[i] * y) % d
else:
    for i in t:
        s = (s * 10 + i) % d

print(s)
