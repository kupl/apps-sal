import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())


MOD = 10**9+7

n = ni()
n_bit = len(bin(n)[2:])

dp = [[0]*4 for _ in range(n_bit+1)]
dp[0][0] = 1

for bit in range(n_bit):
    digit = int(bin(n)[2+bit:2+bit+1])
    
    if digit:
        dp[bit+1][0] = (dp[bit][0]) % MOD
        dp[bit+1][1] = (dp[bit][0] + dp[bit][1]) % MOD
        dp[bit+1][2] = (dp[bit][1]) % MOD
        dp[bit+1][3] = (dp[bit][1] + 3*dp[bit][2] + 3*dp[bit][3]) % MOD
        
    else:
        dp[bit+1][0] = (dp[bit][0] + dp[bit][1]) % MOD
        dp[bit+1][1] = (dp[bit][1]) % MOD
        dp[bit+1][2] = (dp[bit][1] + dp[bit][2]) % MOD
        dp[bit+1][3] = (2*dp[bit][2] + 3*dp[bit][3]) % MOD
        
print(sum(dp[n_bit]) % MOD)
