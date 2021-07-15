# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# library
# -------------------------------------------------------------
class Combination:
    def __init__(self, n, mod):
        self.mod = mod
        self.fact = [1]*n
        self.finv = [1]*n
        self.inv  = [1]*n
        for i in range(2,n):
            self.fact[i] = (self.fact[i-1]*i) % self.mod
            self.inv[i]  = self.mod - self.inv[self.mod%i] * (self.mod//i)%self.mod
            self.finv[i] = self.finv[i-1] * self.inv[i] % self.mod
 
    def nCr(self, n, r):
        if n<r:
            return 0
        else:
            return self.fact[n] * (self.finv[r] * self.finv[n-r] % self.mod) % self.mod

mod = 10**9+7
Combination = Combination(200010, mod)

# -------------------------------------------------------------
# main
# -------------------------------------------------------------

N,M,K = map(int,input().split())

ans = 0
for d in range(1,N):
    t = d * Combination.nCr(N*M-2, K-2)
    t %= mod
    t *= (N-d)*M*M
    t %= mod
    ans += t
    ans %= mod
for d in range(1,M):
    t = d * Combination.nCr(N*M-2, K-2)
    t %= mod
    t *= (M-d)*N*N
    t %= mod
    ans += t
    ans %= mod

print(ans)
