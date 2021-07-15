import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n,m = list(map(int,ipt().split()))
    cos = []
    row = []
    col = []
    for _ in range(m):
        a,b,c = list(map(int,ipt().split()))
        row.append(a-1)
        col.append(b-1)
        cos.append(c)
    csr = csr_matrix((cos,(row,col)),shape=(n,n))
    d = dijkstra(csr,directed=False)
    ans = 0
    for i in range(m):
        rwi = row[i]
        cli = col[i]
        csi = cos[i]
        dri = d[rwi]
        dci = d[cli]
        for j in range(n):
            if dri[j] + csi == dci[j]:
                break
            if j == n-1:
                ans += 1
    print(ans)
    return

def __starting_point():
    main()

__starting_point()
