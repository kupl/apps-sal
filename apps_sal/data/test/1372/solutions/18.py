from sys import stdin
import numpy as np
from numba import njit

H,N = map(int, input().split())
M = [list(map(int, stdin.readline().split())) for i in [0]*N]
M = np.array(M)

@njit
def main(h,n,m):
    dp = [10**8+1]*(10**4+1)
    dp = np.array(dp)
    dp[0] = 0

    for i in range(1,10**4+1):
        for j in range(n):
            a = m[j][0]
            b = m[j][1]
            if a>i:
                dp[i] = min(dp[i],b)
            else:
                dp[i] = min(dp[i],dp[i-a]+b)

    print(dp[h])

def __starting_point():
    main(H,N,M)
__starting_point()
