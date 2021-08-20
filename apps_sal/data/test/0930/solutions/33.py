def cmb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10 ** 9 + 7
N = 2 * 10 ** 5 + 1
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]
for i in range(2, N + 1):
    g1.append(g1[-1] * i % mod)
    inverse.append(-inverse[mod % i] * (mod // i) % mod)
    g2.append(g2[-1] * inverse[-1] % mod)
(a, b) = map(int, input().split())
c = min(a, b)
s = 0
for i in range(0, c + 1):
    s += cmb(a, i, 10 ** 9 + 7) * cmb(a - 1, i, 10 ** 9 + 7)
print(s % (10 ** 9 + 7))
