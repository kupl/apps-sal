from fractions import gcd
3


n = int(input())


def dfs(u, v, nxt, vis):
    if u == v:
        return True
    elif vis[u]:
        return False
    else:
        vis[u] = True
        return dfs(nxt[u], v, nxt, vis)


def size(u, v, nxt):
    if u == v:
        return 1
    return size(nxt[u], v, nxt) + 1


nxt = list(map(int, input().split()))
for i in range(n):
    nxt[i] -= 1

szs = []

for i in range(n):
    if not dfs(nxt[i], i, nxt, [False] * n) and nxt[i] != i:
        print(-1)
        return
    elif nxt[i] == i:
        szs.append(1)
    else:
        szs.append(size(nxt[i], i, nxt))


ans = 1
g = 0
for i in range(n):
    if szs[i] % 2 == 0:
        szs[i] //= 2
    ans = (ans * szs[i]) // gcd(ans, szs[i])

print(ans)
