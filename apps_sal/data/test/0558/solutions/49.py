def cmb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 998244353
nums = 2 * 10 ** 5
(g1, g2, inverse) = ([1, 1], [1, 1], [0, 1])
for num in range(2, nums + 1):
    g1.append(g1[-1] * num % mod)
    inverse.append(-inverse[mod % num] * (mod // num) % mod)
    g2.append(g2[-1] * inverse[-1] % mod)
(n, m, k) = list(map(int, input().split()))
ans = 0
for i in range(k + 1):
    ans += m * cmb(n - 1, i, mod) * pow(m - 1, n - i - 1, mod)
    ans %= mod
print(ans)
