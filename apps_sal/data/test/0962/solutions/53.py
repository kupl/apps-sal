import sys
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 7)

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
import numpy as np
from collections import defaultdict

N,M = map(int,readline().split())

if M == 0:
    print(-1)
    return

AB = [tuple(int(x) for x in line.split()) for line in readlines()]

A,B = zip(*AB)
graph = csr_matrix(([1]*M,(A,B)),(N+1,N+1))
_,comp = connected_components(graph,connection='strong')

size = np.bincount(comp)

if size.max() == 1:
    print(-1)
    return

n = np.where(size > 1)[0][0]

V = set(np.where(comp == n)[0])

graph = [[] for _ in range(N+1)]
for a,b in AB:
    if a in V and b in V:
        graph[a].append(b)

# とりあえず1つサイクルを見つける
order = defaultdict(int)
x = V.pop()
V.add(x)
q = [x]
order[x] = 1
path = [x]
flag = False
while True:
    y = graph[x][0]
    if order[y] != 0:
        path = path[order[y]-1:]
        break
    path.append(y)
    order[y] = order[x] + 1
    x = y

V = set(path)
next_v = {u:v for u,v in zip(path,path[1:])}; next_v[path[-1]] = path[0]

# 辺を1つ追加しながら、小さいサイクルを見つける
for a,b in AB:
    if not (a in V and b in V):
        continue
    # 間の頂点を削除
    x = next_v[a]
    while x != b:
        V.remove(x)
        x = next_v[x]
    next_v[a] = b

print(len(V))
print(*V,sep='\n')


