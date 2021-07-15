import math
import numpy as np
import queue
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n,c = list(map(int,ipt().split()))
    cc = [[] for _ in [0]*c]
    tma = 0
    for i in range(n):
        s,t,c = list(map(int,ipt().split()))
        hpq.heappush(cc[c-1],(s,t))
        if t > tma:
            tma = t
    cnt = np.zeros(tma+1,dtype=int)
    for i in cc:
        ps = -1
        pt = -1
        while len(i) > 0:
            ns,nt = hpq.heappop(i)
            if pt == ns:
                pt = nt
                continue
            elif not pt == -1:
                cnt[ps:pt+1:] += np.ones(pt-ps+1,dtype=int)
            ps = ns
            pt = nt
        if not pt == -1:
            cnt[ps:pt+1:] += np.ones(pt-ps+1,dtype=int)
    print((max(cnt)))
    return

def __starting_point():
    main()

__starting_point()
