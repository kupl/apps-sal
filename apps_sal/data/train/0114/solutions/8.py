import math
import sys
from bisect import bisect_right as bs
for _ in range(int(input())):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    m=int(input())
    ma=-1
    h=[0]*(n+1)
    for i in range(m):
        x,y=list(map(int,sys.stdin.readline().split()))
        ma=max(ma,x)
        h[y]=max(h[y],x)
    
    for i in range(n-1,0,-1):
        h[i]=max(h[i+1],h[i])
    # print(h)    
    if ma<max(a):
        print(-1)
    else:
        ma=-1
        prev=0
        ans=1
        i=0
        while i<n:
            ma=max(a[i],ma)
            # print(ma,i,ans)
            if h[i-prev+1]<ma:
                prev=i
                ans+=1
                ma=-1
            else:
                i+=1
        print(ans)        

