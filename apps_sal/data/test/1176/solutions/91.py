from bisect import bisect_left,bisect,bisect_right
import sys

icase=0
if icase==0:
    n=int(input())
    a=list(map(int,input().split()))

a.sort()
ii=bisect(a,0)

if ii==n:
    if ii%2==0:
        asum=-sum(a)
    else:    
        asum=-sum(a[0:ii-1])+a[ii-1]
    print(asum)
    return

if ii%2==0:
    asum=-sum(a[0:ii])+sum(a[ii:])
else:
    if -a[ii-1]<a[ii]:
        d=a[ii-1]+a[ii]
    else:
        d=-a[ii-1]-a[ii]
    asum=-sum(a[0:ii-1])+d+sum(a[ii+1:])

print(asum)

