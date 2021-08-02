from math import gcd

n = int(input())
crush = list(map(int, input().split()))
crush = [0] + crush

vis, dis, cyc, flag = [0] * (n + 1), [-1] * (n + 1), [], 1


def dfs(u, d):
    dis[u] = d
    vis[u] = 1
    nonlocal flag
    v = crush[u]
    if vis[v] == 0:
        dfs(v, d + 1)
    else:
        if dis[v] == 1:
            cyc.append(d)
        else:
            flag = 0
    dis[u] = -1


for i in range(1, n + 1):
    if not flag:
        break
    if vis[i] == 0:
        dfs(i, 1)


if not flag or len(cyc) == 0:
    print(-1)
else:
    def lcm(a, b):
        return a * b // gcd(a, b)

    L = cyc[0]
    if not L % 2:
        L //= 2
    for i in range(1, len(cyc)):
        s = cyc[i]
        if not s % 2:
            s //= 2
        L = lcm(L, s)
    print(L)


#  C:\Users\Usuario\HOME2\Programacion\ACM
