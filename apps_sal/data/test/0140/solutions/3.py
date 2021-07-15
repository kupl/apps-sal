import sys
from operator import itemgetter
readline = sys.stdin.readline
N, M = map(int, readline().split())
 
inf = 10**9+7

 
XS = [(0, 0)] + [tuple(map(int, readline().split())) for _ in range(N)]
XS.sort(key = lambda x: x[0]-x[1])
x, s = XS[0]

dp1 = [0] + [max(0, x-s-1, j-x-s) for j in range(1, M+2)]
for x, s in XS[1:]:
    
    dp1n = dp1[:]
    
    dp1n[min(M, x+s)] = min(dp1n[min(M, x+s)], dp1[max(0, x-s-1)])
    for j in range(M):
        if x + s + j > M:
            break
        dp1n[x+s+j] = min(dp1n[x+s+j], j + dp1[max(0, x-s-1-j)])
   
    dp1 = dp1n[:]
    
    for i in range(M, -1, -1):
        dp1[i] = min(dp1[i], dp1[i+1])
print(dp1[M]) 
