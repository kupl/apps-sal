N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
mod = 10**9 + 7

fac = [0] * (N + 1)
facinv = [0] * (N + 1)
fac[0] = 1
facinv[0] = 1
for i in range(N):
    fac[i + 1] = (fac[i] * (i + 1)) % mod
    facinv[i + 1] = (facinv[i] * pow(i + 1, -1, mod)) % mod


def nCk(n, k):
    return (fac[n] * facinv[k] * facinv[n - k]) % mod


p = 0
m = 0
for i in range(K - 1, N):
    p = (p + A[i] * nCk(i, K - 1)) % mod
    m = (m + A[N - i - 1] * nCk(i, K - 1)) % mod
    #print(A[i-K+1] , nCk(N-i+1, K-1))

print((p - m) % mod)
