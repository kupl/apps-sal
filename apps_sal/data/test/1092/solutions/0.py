(n, m) = map(int, input().split())
t = sorted(map(int, input().split()))
(f, d) = ([1] * (n + 1), 1000000007)
for i in range(2, n + 1):
    f[i] = f[i - 1] * i % d
(p, q) = (0, f[t[0] - 1] * f[n - t[-1]] % d)
for i in range(m - 1):
    l = t[i + 1] - t[i] - 1
    q = q * f[l] % d
    if l > 1:
        p += l - 1
print(pow(2, p, d) * f[n - m] * pow(q, d - 2, d) % d)
