import sys
from math import gcd

input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    A=[a[i] for i in range(n)]
    A.sort()
    m=min(a)
    check=all(a[i]==A[i] or a[i]%m==0 for i in range(n))
    print("YES" if check else "NO")

