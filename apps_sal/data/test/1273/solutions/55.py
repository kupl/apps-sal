import sys
sys.setrecursionlimit(10**6)
n = int(input())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1] += [(b - 1, i)]
    g[b - 1] += [(a - 1, i)]
l = [0] * (n - 1)


def dfs(v, p=-1, s=-1):
    t = 1
    for c, i in g[v]:
        if c == p:
            continue
        if t == s:
            t += 1
        l[i] = t
        dfs(c, v, t)
        t += 1


dfs(0)
print(max(l))
for i in l:
    print(i)
