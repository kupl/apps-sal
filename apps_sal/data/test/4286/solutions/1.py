n, m = map(int, input().split())
a = list(map(int, input().split()))
e = []
for _ in range(m) : 
    u, v, w = map(int, input().split())
    e.append((u-1, v-1, w))
a = sorted(zip(a, range(n)), key = lambda x : x[0])
for i in range(1, n) : 
    e.append((a[0][1], a[i][1], a[0][0] + a[i][0]))

fa = list(range(n))
rk = [0] * n

def find(x) :
    while fa[x] != x :
        fa[x] = fa[fa[x]]
        x = fa[x]
    return x

def unite(u, v) :
    u, v = map(find, (u, v))
    if u == v : return False
    if rk[u] < rk[v] : u, v = v, u
    fa[v] = u
    if rk[u] == rk[v] : rk[u] += 1
    return True

e.sort(key = lambda x : x[2])

ans = 0
cnt = 1
for ee in e :
    if cnt == n : break
    if unite(ee[0], ee[1]) :
        ans += ee[2]
        cnt += 1

print(ans)
