import sys
def input():
    return sys.stdin.readline()[:-1]
import heapq
N,C=map(int,input().split())
a=0
x=[0]*N
v=[0]*N
for i in range(N):
    x[i],v[i]=map(int,input().split())
h=[0]
s=t=sum(v)
for i in range(N-1,-1,-1):
    k=t-x[i]-h[0]
    if k>a:
        a=k
    t-=v[i]
    heapq.heappush(h,t-s+2*(C-x[i]))
h=[0]
t=s
for i in range(N):
    k=t-C+x[i]-h[0]
    if k>a:
        a=k
    t-=v[i]
    heapq.heappush(h,t-s+2*x[i])
print(a)
