import sys
sys.setrecursionlimit(1000000000)
def ii(): return int(input())
def ii0(): return ii() - 1
def mis(): return list(map(int, input().split()))
def lmis(): return list(mis())


INF = float('inf')


def main():
    N, M, L = mis()
    from scipy.sparse.csgraph import floyd_warshall
    import numpy as np
    INF = np.iinfo(np.int64).max
    d = np.full((N, N), INF, dtype=np.uint64)
    for i in range(N):
        d[i, i] = 0
    for _ in range(M):
        a, b, c = mis()
        a -= 1
        b -= 1
        if c <= L:
            d[a, b] = c
            d[b, a] = c
    '''
    for k in range(N):
        for i in range(N):
            np.minimum(d[i,:], d[i,k]+d[k,:], out=d[i,:])    
    '''
    d = floyd_warshall(d)
    d2 = np.full((N, N), INF, dtype=np.uint64)
    for i in range(N):
        d2[i, i] = 0
    for i in range(N):
        for j in range(N):
            if d[i, j] <= L:
                d2[i, j] = 1
    '''
    for k in range(N):
        for i in range(N):
            np.minimum(d2[i,:], d2[i,k]+d2[k,:], out=d2[i,:])    
    '''
    d2 = floyd_warshall(d2)
    Q = ii()
    for _ in range(Q):
        s, t = mis()
        s -= 1
        t -= 1
        dist = d2[s, t]
        if dist == INF:
            print((-1))
        else:
            print((int(dist) - 1))


main()
