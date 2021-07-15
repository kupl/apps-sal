import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())
G = [[] for i in range(N)]

for i in range(M):
  a,b = map(int,readline().split())
  G[a - 1].append(b - 1)
  G[b - 1].append(a - 1)
  
for child in G[0]:
  for gchild in G[child]:
    if gchild == N - 1:
      print("POSSIBLE")
      return
print("IMPOSSIBLE")  
