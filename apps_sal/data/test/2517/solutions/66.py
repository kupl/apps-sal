import numpy as np
from scipy.sparse.csgraph import dijkstra

N,M,R = list(map(int,input().split()))
r = list(map(int,input().split()))
for i in range(R):
    r[i] -= 1

connections = np.zeros((N,N))
for i in range(M):
    A,B,C = list(map(int,input().split()))
    A,B = A-1,B-1
    
    connections[A][B] = C
    connections[B][A] = C

connections = dijkstra(connections)

def explore(unvisited,total,start):
    if unvisited:
        ret = float('inf')
        for town in unvisited:
            ret = min(ret,explore(unvisited-set([town]),
                total+connections[start][town],town))
        return ret
    else:
        return total

ans = float('inf')
targets = set(r)
for s in r:
    ans = min(ans,explore(targets-set([s]),0,s))
print(int(ans))
