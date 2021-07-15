def find(x):
  if par[x] == x:
    return x
  else:
    par[x] = find(par[x]) #経路圧縮
    return par[x]
  
def same(x,y):
  return find(x) == find(y)

def unite(x,y):
  x = find(x)
  y = find(y)
  if x == y:
    return 0
  par[x] = y

def groups(par):
    leader_buf = [find(par[i]) for i in range(len(par))]
    result = [[] for _ in range(len(par))]
    for i in range(len(par)): result[leader_buf[i]].append(i)
    return [r for r in result if r != []]
  
n,m = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

par = [[] for _ in range(n+1)]
for i in range(n+1):
  par[i] = i
  
for i in range(m):
  c,d = map(int, input().split())
  unite(c,d)
  
g = groups(par)

for i in range(1,len(g)):
  asum = 0
  bsum = 0
  for j in range(len(g[i])):
    asum += a[g[i][j]-1]
    bsum += b[g[i][j]-1]
  if asum != bsum:
    print("No")
    return
    
print("Yes")
