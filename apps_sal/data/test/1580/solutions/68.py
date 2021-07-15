n,m = map(int,input().split())


par = [-1]*(n)
def find(x):
    if par[x] < 0:
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
    else:
      if par[x] > par[y]:x,y = y,x
      par[x] += par[y]
      par[y] = x
def size(x):
    return -par[find(x)]


for i in range(m):
  x,y,z = map(int,input().split())
  unite(x-1,y-1)


ans = 0
# print(par)
for i in range(n):
  if par[i] <0:
    ans += 1
print(ans)
