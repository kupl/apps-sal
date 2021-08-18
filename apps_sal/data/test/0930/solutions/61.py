def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10**9 + 7
N = 10**6
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)
a, b = map(int, input().split())
mod = (10**9) + 7
if b >= a - 1:
    print(cmb((2 * a) - 1, a, mod))
else:
    ans = 0
    for i in range(1, b + 1):
        ans += cmb(a, i, mod) * cmb(a - 1, a - i - 1, mod)
    if b != 1:
        ans += 1
    print(ans % mod)
