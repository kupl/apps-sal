import sys
from math import log2,floor,ceil,sqrt
# import bisect
# from collections import deque

Ri = lambda : [int(x) for x in sys.stdin.readline().split()]
ri = lambda : sys.stdin.readline().strip()
 
def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
INF = 10 ** 18
MOD = 10**9+7

n = int(ri())
st = ri()
st = [ord(st[i])-ord('a') for i in range(len(st))]

dp = list2d(26,n+1,0)
for i in range(0,26):
    for j in range(n):
        cnt=  0
        for k in range(j,n):
            if st[k] != i:
                cnt+=1
            dp[i][cnt] = max(k-j+1,dp[i][cnt])

for i in range(26):
    for j in range(1,n+1):
        dp[i][j] = max(dp[i][j-1],dp[i][j])

# print(dp)

qq = int(ri())
for i in range(qq):
    temp= ri().split()
    ch = ord(temp[1])-ord('a')
    # print(dp[ch])
    m = int(temp[0])
    if m > n:
        m = n
    # print(ch,m)
    print(dp[ch][m])

