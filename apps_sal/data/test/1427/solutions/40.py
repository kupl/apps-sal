#

import sys
from fractions import gcd
input=sys.stdin.readline

def main():
    MOD=10**9+7
    N=int(input())
    A=list(map(int,input().split()))
    if N==1:
        print((1))
        return
    l=(A[0]*A[1])//gcd(A[0],A[1])
    for i in range(2,N):
        l=(l*A[i])//gcd(A[i],l-A[i])
    l%=MOD
    ans=0
    for i in range(N):
        ans+=l*pow(A[i],MOD-2,MOD)
        ans%=MOD
    print(ans)
    
    
    
def __starting_point():
    main()

__starting_point()
