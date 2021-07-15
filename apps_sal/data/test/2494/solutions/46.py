import sys
from collections import deque
readline=sys.stdin.readline

def main():
    k=int(readline())
    v=list(range(k))
    inf=float('inf')
    dist=[inf]*k
    visited=[0]*k
    stack=deque([1])
    dist[1]=0
    while stack:
        v=stack.pop()
        if not visited[v]:
            nv0=10*v%k
            nv1=(v+1)%k
            if dist[nv0]>dist[v]:
                dist[nv0]=dist[v]
                stack.append(nv0)
            if dist[nv1]>dist[v]+1:
                dist[nv1]=dist[v]+1
                stack.appendleft(nv1)
            visited[v]=1
    print((dist[0]+1))

def __starting_point():
    main()

__starting_point()
