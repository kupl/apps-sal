import sys
sys.setrecursionlimit(10**9)
n = int(input())
t = [[] for _ in range(n)]
for i in range(n-1):
  a,b,c = map(int,input().split())
  t[a-1].append((b-1,c))
  t[b-1].append((a-1,c))
q,k = map(int,input().split())
k -= 1
l = [0]*n
def dfs(a,b,c):
  for i,j in t[b]:
    if i != a:
      l[i] = c+j
      dfs(b,i,c+j)
dfs(-1,k,0)
for _ in range(q):
  x,y = map(lambda x:int(x)-1,input().split())
  print(l[x]+l[y])
