import io,os
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
import sys
from collections import deque

def solve(n,m,Edges,T):
    if n==1:
        if T[0]==1:
            return [1]
        return [-1]
    L=[]
    for i,t in enumerate(T):
        L.append((t,i))
    L.sort()
    Visited=[False]*n
    Ans=[]
    for num,fr in L:
        Visited[fr]=True
        s=set()
        for to in Edges[fr]:
            if Visited[to]:
                if T[to]==num:
                    return [-1]
                s.add(T[to])
        if len(s)!=num-1:
            return [-1]
        Ans.append(fr+1)
    return Ans

def main():
    n,m=map(int,input().split())
    Edges=[[] for _ in range(n)]
    for _ in range(m):
        a,b=map(lambda x: int(x)-1,input().split())
        Edges[a].append(b)
        Edges[b].append(a)
    T=list(map(int,input().split()))
    Ans=solve(n,m,Edges,T)
    sys.stdout.write(' '.join(map(str,Ans))+'\n')
    
def __starting_point():
    main()
__starting_point()
