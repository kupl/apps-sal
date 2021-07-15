def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x,y):
    x, y = find(x), find(y)
    if x == y:
        return False
    
    if par[x] > par[y]:
        x,y = y,x
    par[x] += par[y]
    par[y] = x
    return True

def size(x):
    return -par[find(x)]

n, m = map(int, input().split())
ab = []
for _ in range(m):
    a, b = map(int, input().split())
    ab.append([a-1, b-1])
par = [-1]*n
ans = n*(n-1)//2
ansl = [ans]
for a, b in ab[::-1]:
    if find(a)!=find(b):
        ans -= size(a)*size(b)
    unite(a, b)
    ansl.append(ans)
for i in range(m-1, -1, -1):
    print(ansl[i])
