from heapq import heappop,heappush

n,m = list(map(int,input().split()))

C = [[] for _ in range(n)]
indeg = [0]*n

def toposort():
    S = [i for i in range(n) if indeg[i] == 0]
    nparent = indeg[:]
    topo = []
    while S:
        cur = S.pop()
        topo.append(cur)
        for neigh,_ in C[cur]:
            nparent[neigh] -= 1
            if nparent[neigh] == 0:
                S.append(neigh)
    return topo

def solve():
    topo = toposort()

    D = [(0,0)]*n
    for cur in topo:
        for neigh,t in C[cur]:
            cd,ct = D[cur]
            nd,_ = D[neigh]
            if nd <= cd + 1:
                D[neigh] = cd + 1, max(ct,t)

    d,t = max(D)
    return t+1 if d == n-1 else -1
        

for _ in range(m):
    a,b = list(map(int,input().split()))
    C[a-1].append((b-1, _))
    indeg[b-1] += 1

print(solve())

