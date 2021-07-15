from networkx import *
N,M = map(int,input().split())
A = [list(map(int,input().split())) for m in range(M)]
G = Graph(A)
ans = 0

for n in range(2,N+1):
  for p in all_simple_paths(G,1,n):
    if len(p)==N:
      ans+=1

print(ans)
