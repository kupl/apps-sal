import sys
sys.setrecursionlimit(10 ** 9)
n = int(input())
to = [[] for i in range(n)]
edge = {}
color = [0] * (n - 1)
for i in range(1, n):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)
    edge[a, b] = edge[b, a] = i


def dfs(n, b=-1, bc=-1):
    to_n = to[n]
    k = 1
    for i in range(len(to_n)):
        if to_n[i] == b:
            continue
        if k == bc:
            k += 1
        color[edge[n, to_n[i]] - 1] = k
        dfs(to_n[i], n, k)
        k += 1


dfs(0)
print(max(color))
for i in range(n - 1):
    print(color[i])
