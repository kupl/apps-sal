MOD = 10**9 + 7

class Combinatorics:
    def __init__(self, N, mod):
        '''
        Preprocess for calculating binomial coefficients nCr (0 <= r <= n, 0 <= n <= N)
        over the finite field Z/(mod)Z.
        Input:
            N (int): maximum n
            mod (int): a prime number. The order of the field Z/(mod)Z over which nCr is calculated.
        '''
        self.mod = mod
        self.fact = [0] * (N+1)           # n!
        self.inverse = [None] + [0] * N   # inverse of n in the field Z/(MOD)Z
        self.fact_inverse = [0] * (N+1)   # inverse of n! in the field Z/(MOD)Z
        
        # preprocess
        self.fact[0] = self.fact[1] = 1
        self.fact_inverse[0] = self.fact_inverse[1] = 1
        self.inverse[1] = 1
        for i in range(2, N+1):
            self.fact[i] = i * self.fact[i-1] % self.mod
            q, r = divmod(self.mod, i)
            self.inverse[i] = (- (q % self.mod) * self.inverse[r]) % self.mod
            self.fact_inverse[i] = self.inverse[i] * self.fact_inverse[i-1] % self.mod
    
    def perm(self, n, r):
        '''
        Calculate nPr = n! / (n-r)! % mod
        '''
        if n < r or n < 0 or r < 0: return 0
        else: return (self.fact[n] * self.fact_inverse[n-r]) % self.mod
    
    def binom(self, n, r):
        '''
        Calculate nCr = n! /(r! (n-r)!) % mod
        '''
        if n < r or n < 0 or r < 0: return 0
        else: return self.fact[n] * (self.fact_inverse[r] * self.fact_inverse[n-r] % self.mod) % self.mod
        
    def hom(self, n, r):
        '''
        Calculate nHr = {n+r-1}Cr % mod.
        Assign r objects to one of n classes.
        Arrangement of r circles and n-1 partitions:
            o o o | o o | | | o | | | o o | | o
        '''
        if n == 0 and r > 0: return 0
        if n >= 0 and r == 0: return 1
        return self.binom(n + r - 1, r)

N, M = map(int, input().split())
com = Combinatorics(M, MOD)
ans = 0
for i in range(N+1):
    temp = com.perm(M, N)
    temp *= com.binom(N, i); temp %= MOD
    temp *= com.perm(M-i, N-i); temp %= MOD
    ans += ((-1)**i) * temp; ans %= MOD
print(ans)
