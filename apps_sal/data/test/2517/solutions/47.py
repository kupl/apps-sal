from scipy.sparse.csgraph import csgraph_from_dense,dijkstra,floyd_warshall
N,M,R = map(int,input().split())

machi = list(map(int,input().split()))

List = [[10**6]*(N) for i in range(N)]
for i in range(M):
  a,b,c = map(int,input().split())
  
  if List[a-1][b-1] > c:
    List[a-1][b-1] = c
    List[b-1][a-1] = c
G = csgraph_from_dense(List, null_value=10**6)
d = floyd_warshall(G)

import itertools
a = list(itertools.permutations(machi))
arr = []
for i in a:
  ans = 0
  for j in range(R):
    if j != R-1 :
      ans += d[i[j]-1][i[j+1]-1]
  arr.append(ans) 
  
print(int(min(arr)))
