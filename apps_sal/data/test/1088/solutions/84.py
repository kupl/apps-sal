mod = 998244353
fact = [1]
for i in range(1, 51):
    x = i * fact[-1] % mod
    fact.append(x)
(n, k) = list(map(int, input().split()))


def dfs(node):
    if vis[node]:
        return 0
    vis[node] = 1
    ans = 1
    for i in m[node]:
        ans += dfs(i)
    return ans


l = []
for i in range(n):
    l.append(list(map(int, input().split())))
m = []
for i in range(n):
    m.append([])
for i in range(n):
    for j in range(i + 1, n):
        e = 1
        for b in range(n):
            if l[i][b] + l[j][b] > k:
                e = 0
                break
        if e:
            m[i].append(j)
            m[j].append(i)
a = 1
b = 1
vis = [0] * n
for i in range(n):
    x = dfs(i)
    a = a * fact[x] % mod
m = []
for i in range(n):
    m.append([])
for i in range(n):
    for j in range(i + 1, n):
        e = 1
        for v in range(n):
            if l[v][i] + l[v][j] > k:
                e = 0
                break
        if e:
            m[i].append(j)
            m[j].append(i)
vis = [0] * n
for i in range(n):
    x = dfs(i)
    b = b * fact[x] % mod
ans = a * b % mod
print(ans)
