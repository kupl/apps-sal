ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
def ncr(n,r):
    ret = 1
    if n<r:
        return 0
    if n-r <r:
        r = n-r
    for i in range(1,r+1):
        ret*=(n-r+i)
        ret//=i
    return ret

n,a = ma()
X = lma()
for i in range(n):
    X[i] -= a
co = collections.Counter(X)
ans = 0
mx = 49*n #ずれの最大はA=1,x=50 2*mx +1この配列
dp = [[0 for j in range(-mx,mx+1)] for i in range(n+1)]# dp[i][j] iまで使って値をjにする組み合わせ
dp[-1][0] = 1 #一個も使わない組み合わせ
for i in range(n):
    x = X[i]
    #print(x)
    for j in range(-mx,mx+1,1):
        dp[i][j] += dp[i-1][j] + dp[i-1][j-x] #選ばない/ぶ
        #if j==0:print(i,j,dp[i-1][j] , dp[i-1][j-x])
print(dp[n-1][0]-1)

