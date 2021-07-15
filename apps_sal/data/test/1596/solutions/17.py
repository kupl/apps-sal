
from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

S = input()
L = len(S)

N = 10**5 + 5
dp = [0]*N
dp[1] = 1
dp[2] = 2
for i in range(3,N):
    dp[i] = (dp[i-1] + dp[i-2]) %mod

S += 'X'
i = 0
ans = 1
while i < L:
    if S[i] == 'u':
        cnt = 0
        while S[i] == 'u':
            i += 1
            cnt += 1
        ans *= dp[cnt]
    elif S[i] == 'n':
        cnt = 0
        while S[i] == 'n':
            i += 1
            cnt += 1
        ans *= dp[cnt]
    elif S[i] == 'm' or S[i] == 'w':
        print(0)
        return
    else:
        i += 1
    ans %= mod
print(ans%mod)

