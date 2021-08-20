(N, K) = list(map(int, input().split()))
R = N - K
mod = 10 ** 9 + 7
fac = [0] * 2010
facinv = [0] * 2010
fac[1] = 1
facinv[1] = pow(1, -1, mod)
fac[0] = 1
facinv[0] = 1
for i in range(2, 2000):
    fac[i] = fac[i - 1] * i % mod
    facinv[i] = facinv[i - 1] * pow(i, -1, mod) % mod


def nCk(n, k):
    return fac[n] * facinv[k] * facinv[n - k] % mod


for i in range(K):
    if i > R:
        print('0')
    else:
        print(nCk(K - 1, i) * nCk(R + 1, i + 1) % mod)
