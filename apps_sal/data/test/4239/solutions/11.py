import sys
sys.setrecursionlimit(10**8)

N = int(input())

ss = set()
n = 6
while n <= 10**5:
    ss.add(n)
    n *= 6
n = 9
while n <= 10**5:
    ss.add(n)
    n *= 9

dp = [None] * (N+1)

def rec(n):
    if dp[n] is not None:
        return dp[n]
    tmp = n
    for s in ss:
        if s > n: continue
        if s == n:
            tmp = 1
            break
        tmp = min(tmp, 1 + rec(n-s))
    dp[n] = tmp
    return tmp

print(rec(N))
