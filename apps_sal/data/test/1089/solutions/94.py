import sys
input = sys.stdin.readline
import copy

def main():
    N,M,K = list(map(int,input().split()))
    MOD = 10**9+7
    fac = [0 for _ in range(N*M-1)]
    fac[0],fac[1] = 1,1
    inv = copy.deepcopy(fac)
    invfac = copy.deepcopy(fac)
    
    for i in range(2,N*M-1):
        fac[i] = (fac[i-1]*i)%MOD
        inv[i] = MOD-(MOD//i)*inv[MOD%i]%MOD
        invfac[i] = (invfac[i-1]*inv[i])%MOD
        
    def coef(x,y):
        num = (((fac[x]*invfac[y])%MOD)*invfac[x-y]%MOD)
        return num

    xa = ((M**2)*N*(N-1)*(N+1)//6)%MOD
    ya = ((N**2)*M*(M-1)*(M+1)//6)%MOD
    print(((xa+ya)*coef(N*M-2,K-2)%MOD))

def __starting_point():
    main()

__starting_point()
