import sys
from heapq import heapify, heappop
from bisect import bisect_left, bisect_right, insort_left
read=sys.stdin.read
readline=sys.stdin.readline

def main():
    n=int(readline())
    t,v=(list(map(int,l.split())) for l in read().splitlines())
    vi=[(x,i+1) for i,x in enumerate(v)]
    x=[0]*(n+2)
    y=[0]*(n+1)
    x[0]=0
    y[0]=0
    y[-1]=0
    for i in range(1,n+1):
        x[i]=x[i-1]+t[i-1]
    x[n+1]=x[n]
    heapify(vi)
    ans=0
    v=[0]+v+[0]
    memo=[0,n+1]
    while vi:
        e=heappop(vi)
        insort_left(memo,e[1])
        idx=bisect_left(memo,e[1])
        _i=memo[idx-1]
        i_=memo[idx+1]
        i=memo[idx]
        sx=x[_i]
        gx=x[i_-1]
        sy=y[_i]
        gy=y[i_-1]
        h=e[0]
        y[i]=min(h,gx-x[i]+gy,x[i]-sx+sy)
        y[i-1]=min(h,gx-x[i-1]+gy,x[i-1]-sx+sy)
        dw=gx-sx
        dh=abs(gy-sy)
        be=max(0,dw-(2*max(v[_i],v[i_])-sy-gy))
        ht=min(h-v[_i],h-v[i_],be/2)
        te=max(0,be-2*ht)
        ans+=(te+be)*ht/2
    print(ans)

def __starting_point():
    main()

__starting_point()
