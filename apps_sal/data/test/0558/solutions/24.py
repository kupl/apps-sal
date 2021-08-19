import sys
read = sys.stdin.read
readline = sys.stdin.readline


def cmb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


def make_table2(n, mod=10 ** 9 + 7):
    g1 = [0] * (n + 1)
    g1[0] = 1
    g1[1] = 1
    tmp = 1
    for i in range(2, n + 1):
        tmp = tmp * i % mod
        g1[i] = tmp
    g2 = [0] * (n + 1)
    g2[-1] = pow(g1[-1], mod - 2, mod)
    tmp = g2[-1]
    for i in range(n - 1, -1, -1):
        tmp = tmp * (i + 1) % mod
        g2[i] = tmp
    return (g1, g2)


(N, M, K) = list(map(int, read().split()))
mod = 998244353
(g1, g2) = make_table2(N, mod)
answer = 0
for i in range(K + 1):
    answer = (answer + cmb(N - 1, i, mod) * M * pow(M - 1, N - i - 1, mod)) % mod
print(answer)
