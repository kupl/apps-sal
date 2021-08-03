n, k = map(int, input().split())
mod = 10**9 + 7
if n <= k:
    l = 2 * n - 1
    inverse = [0, 1]
    g = [1, 1]
    for i in range(2, n):
        l *= 2 * n - i
        l %= mod
        inverse.append(-inverse[mod % i] * (mod // i) % mod)
        g.append(g[-1] * inverse[-1] % mod)
    print(l * g[-1] % mod)
else:
    h = [1, 1]
    g = [1, 1]
    inverse = [0, 1]
    for i in range(2, 2 * n + 1):
        h.append(h[-1] * i % mod)
        inverse.append(-inverse[mod % i] * (mod // i) % mod)
        g.append(g[-1] * inverse[-1] % mod)

    def comb(a, b): return h[a] * g[b] * g[a - b] % mod
    # i手かけないとたどり着けないやつ
    t = [comb(n, i) * comb(n - 1, i) % mod for i in range(k + 1)]
    print(sum(t) % mod)
