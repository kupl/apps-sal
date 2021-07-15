MOD = 10 **9 + 7
INF = 10 ** 10
import numpy as np
from  scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

def main():
    n,m,l = map(int,input().split())
    dist = [[np.inf] * n for _ in range(n)]  
    for _ in range(m):
        a,b,c = map(int,input().split())
        a -= 1
        b -= 1
        dist[a][b] = c
        dist[b][a] = c

    csr = csr_matrix(dist)
    dist1 = floyd_warshall(csr,directed = False)
    dist1 = np.where(dist1 <= l,1,np.inf)
    cnt = floyd_warshall(dist1,directed = False)
    cnt[cnt == np.inf] = 0
    cnt = cnt.astype(int)
    q = int(input())
    for _ in range(q):
        s,t = map(int,input().split())
        s -= 1
        t -= 1
        print(cnt[s][t] - 1)
def __starting_point():
    main()
__starting_point()
