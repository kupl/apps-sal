n, m = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
fa = [0] + [i + 1 for i in range(n)]

def findFa(x):
    s = []
    while fa[x] != x:
        s.append(x)
        x = fa[x]
    for v in s:
        fa[v] = x
    return x

while m:
    u, v = list(map(int, input().split()))
    u = findFa(u)
    v = findFa(v)
    if u != v:
        fa[v] = u
        a[u] = min(a[u], a[v])
    m -= 1
res = 0
for i in range(1, n + 1):
    if findFa(i) == i:
        res += a[fa[i]]
print(res)


