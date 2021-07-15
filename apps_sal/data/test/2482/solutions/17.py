from collections import Counter
n, k, l = map(int, input().split())
def find(x, par):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x], par)
        return par[x]
def unite(x, y, par):
    p = find(x, par)
    q = find(y, par)
    if p == q:
        return None
    if p > q:
        p, q = q, p
    par[p] += par[q]
    par[q] = p
def same(x, y):
    return find(x) == find(y)
def size(x):
    return -par[find(x)]
road_par = [-1 for i in range(n + 1)]
train_par = [-1 for i in range(n + 1)]
for i in range(k):
    p, q = map(int, input().split())
    unite(p, q, road_par)
for i in range(l):
    r, s = map(int, input().split())
    unite(r, s, train_par)
ans = []
for i in range(n):
    ans.append((find(i + 1, road_par), find(i + 1, train_par)))
c = Counter(ans)
for i in ans:
    print(c[i], end=" ")
