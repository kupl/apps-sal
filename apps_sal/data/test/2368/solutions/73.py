n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
par = [i for i in range(n+1)]

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
    
for i in range(m):
  s,t = map(int,input().split())
  unite(s,t)

for i in range(n+1):
  par[i] = find(i)

data = [0 for _ in range(n+1)]
for i in range(1,n+1):
  data[par[i]] += a[i-1]
  data[par[i]] -= b[i-1]


if data.count(0) == n+1:
  print("Yes")
else:
  print("No")
