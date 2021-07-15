import numpy as np
MAX = 200002
MOD = 998244353
fac = np.zeros(MAX)
finv = np.zeros(MAX)
inv = np.zeros(MAX)

fac[0] = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1
for i in range(2,MAX):
    fac[i] = int(fac[i-1]) * i % MOD
    inv[i] = MOD - int(inv[MOD%i]) * (MOD//i) % MOD
    finv[i] = int(finv[i-1]) * int(inv[i]) % MOD

def COM(N,K):
    return  int(fac[N]) * (int(finv[K]) * int(finv[N - K]) % MOD) % MOD

def resolve():
    N,M,K = map(int,input().split())
    ans = 0
    for i in range(K + 1):
        ans_k = M * COM(N-1, i )
        ans_k = ans_k * pow(M-1,N-1-i, MOD) % MOD
        ans = (ans + ans_k) % MOD
    print(ans)
resolve()
