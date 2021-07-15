import sys
import numpy as np

sys.setrecursionlimit(10 ** 9)
#def input():
#    return sys.stdin.readline()[:-1]

N = int(input())
#X, Y = map(int,input().split())
A = list(map(int,input().split()))

B = []
for i in range(N):
    B.append([A[i], i])
B.sort(reverse=True)

#dp = [[0 for _ in range(N+2)] for _ in range(N+2)]
#for x in range(1,N+2):
#    for y in range(1,N+2):
##        print(act,i)
#        dp[x][y] = max(dp[x-1][y] + B[y][0] * (B[y][1] - 0 - (x-2))
#                    , dp[x][y-1] + B[y][0] * (N - 1 - B[y][1] - (y-2)))
        
dp = np.zeros(1, dtype=int)
zero = np.zeros(1, dtype=int)
for act, i in B:
    prev = dp.copy()
    dp = np.append(dp,[0])
    l = len(prev)
        
    right = np.arange((N-1-i)*act,(N-1-i)*act - (act*(l)),-act)
    left = np.arange(i*act-(act*(l-1)),(i+1)*act,act)
#    print(left,right,prev,dp)
    np.maximum(np.concatenate([prev + left, zero]),
               np.concatenate([zero, prev + right]),
               out = dp)
#    print(dp)

print(np.max(dp))
