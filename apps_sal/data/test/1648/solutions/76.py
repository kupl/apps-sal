(N, K) = map(int, input().split())
R = N - K
M = 10 ** 9 + 7


def cmb(n, r, m):
    f = [1, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] * i % m)
    return f[n] * pow(f[r] * f[n - r] % m, m - 2, m) % m


for i in range(1, K + 1):
    if i <= R + 1:
        Q = cmb(R + 1, i, M) * cmb(K - 1, i - 1, M)
        Q %= M
        print(Q)
    else:
        print(0)
