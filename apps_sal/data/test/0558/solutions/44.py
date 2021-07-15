#import numpy as np
import math
#from decimal import *
#from numba import njit
#@njit
def main():
    (N, M, K) = list(map(int, input().split()))
    MOD = 998244353
    
    fact = [1]*(N+1)
    factinv = [1]*(N+1)
    for i in range(1,N+1):
        fact[i] = fact[i-1]*i % MOD
        factinv[i] = pow(fact[i], MOD-2, MOD)
    def comb(n, k):
        return fact[n] * factinv[k] * factinv[n-k] % MOD

    ans = 0
    for k in range(K+1):
        ans += (comb(N-1,k)*M*pow(M-1, N-k-1, MOD))%MOD

    print((ans%MOD))

main()

