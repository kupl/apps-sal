import sys
import bisect
def input(): return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    A=[0]*n
    for i in range(1,n+1):
        A[-i]=int(input())
    inf=10**10    
    dp=[inf]*(n+1)
    dp[0]=0
    for AA in A:
        bis=bisect.bisect_right(dp, AA)
        dp[bis]=AA #n以下の個数を数える
    print(bisect.bisect_right(dp, inf-100)-1)


def __starting_point():
    main()
__starting_point()
