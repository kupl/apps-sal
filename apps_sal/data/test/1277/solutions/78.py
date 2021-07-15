import sys
sys.setrecursionlimit(1000000)

def dfs_a(N,v,adjlist,cur):
    nonlocal depth_a
    depth_a[v]=cur
    for node in adjlist[v]:
        if depth_a[node]<0:
            dfs_a(N,node,adjlist,cur+1)
def dfs_t(N,v,adjlist,cur):
    nonlocal depth_t
    depth_t[v]=cur
    for node in adjlist[v]:
        if depth_t[node]<0:
            dfs_t(N,node,adjlist,cur+1)
    
    
    

from collections import deque

N,u,v=list(map(int,input().split()))
adjlist=[[] for _ in range(N)]
for _ in range(N-1):
    a,b=list(map(int,input().split()))
    adjlist[a-1].append(b-1)
    adjlist[b-1].append(a-1)
depth_a=[-1]*N
depth_t=[-1]*N
dfs_a(N,v-1,adjlist,0)
dfs_t(N,u-1,adjlist,0)
M=0
for i in range(N):
    if depth_a[i]>depth_t[i]:
        curm=depth_a[i]-1
        if curm>M:
            M=curm
print(M)
        

 
        

