import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

import numpy as np
from scipy.sparse.csgraph import floyd_warshall

n = ni()
g = np.zeros((n,n))
for i in range(n):
    g[i,:] = np.array(list(li()))
    
    
dist = floyd_warshall(g, directed=False)

consis = True
for i in range(n):
    for j in range(n):
        if g[i,j] != dist[i,j]:
            consis = False
            break
        
if not consis:
    print(-1)
    
else:
    total = 0
    INF = float("inf")
    
    for i in range(n):
        dist[i,i] = INF
        
    for i in range(n):
        for j in range(i+1,n):
            via_k = np.min(dist[i] + dist[j])
            
            if via_k > dist[i,j]:
                total += dist[i,j]
                
    print(int(total))
