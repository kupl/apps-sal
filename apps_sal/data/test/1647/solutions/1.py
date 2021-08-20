n = int(input())
v = input()
t = input()
rank = [0] * 26
par = [i for i in range(26)]


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] > rank[y]:
        par[y] = x
    else:
        par[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def same(x, y):
    return find(x) == find(y)


rec = []
num = 0
for i in range(n):
    (a, b) = (ord(v[i]) - ord('a'), ord(t[i]) - ord('a'))
    if not same(a - 1, b - 1):
        unite(a - 1, b - 1)
        rec.append((v[i], t[i]))
        num += 1
print(num)
for (p, q) in rec:
    print(p, q)
