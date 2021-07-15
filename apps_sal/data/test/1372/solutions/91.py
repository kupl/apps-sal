import sys
def input(): return sys.stdin.readline().rstrip()
import numpy as np
def main():
    h,n=map(int,input().split())
    lis=np.array([list(map(int,input().split())) for _ in range(n)])
    a_max=np.max(lis[:,0])
    dp=np.zeros(h+a_max+1,int)
    for i in range(a_max+1,a_max+h+1):
        dp[i]=np.min(dp[i-lis[:,0]]+lis[:,1])
    print(dp[a_max+h])

def __starting_point():
    main()
__starting_point()
