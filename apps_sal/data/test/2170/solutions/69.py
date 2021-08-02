N, M = map(int, input().split())
mod = 10**9 + 7
leng = 500010
fac = [1, 1]
for i in range(2, 500010):
    fac.append(fac[-1] * i % mod)

invfac = [0] * 500010
invfac[500009] = pow(fac[500009], -1, mod)
for i in range(500009):
    invfac[500008 - i] = invfac[500009 - i] * (500009 - i) % mod


def combi(n, m):
    return(fac[n] * invfac[m] * invfac[n - m] % mod)


def permu(n, m):
    return(fac[n] * invfac[n - m] % mod)


Ans = 0

for i in range(N + 1):
    if i % 2 == 0:
        Ans += combi(N, i) * permu(M, i) * (permu(M - i, N - i)**2)
    else:
        Ans -= combi(N, i) * permu(M, i) * (permu(M - i, N - i)**2)

print(Ans % mod)
