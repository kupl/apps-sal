from collections import defaultdict

def solve():

 a = input().strip()
 n = len(a)
 #print(n)
 g = defaultdict(list)
 for i in range(n):
  g[a[i]].append(i)
 vis = {}
 vis[0] = 0
 q = [0]
 # print(g)
 while len(q)!=0:
  tmp = q.pop(0)
  if tmp==n-1:
   break
  val = a[tmp]
  x = len(g[val])
  for i in range(x):
   if g[val][i] not in vis:
    q.append(g[val][i])
    vis[g[val][i]] = vis[tmp]+1
  g[val] = []
  if tmp+1<=n-1 and tmp+1 not in vis:
   q.append(tmp+1)
   vis[tmp+1] = vis[tmp]+1
  if tmp-1>=0 and tmp-1 not in vis:
   q.append(tmp-1)
   vis[tmp-1] = vis[tmp]+1
 print(vis[n-1])


def __starting_point():
 solve()
__starting_point()
