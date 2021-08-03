from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10 ** 7)

n, q = map(int, input().split())

node = [[] for _ in range(n + 1)]
counter = [0 for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
point_dic = defaultdict(int)

for _ in range(n - 1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for _ in range(q):
    p, x = map(int, input().split())
    point_dic[p] += x


def dfs(now, before):
    nonlocal counter
    nonlocal visited

    if visited[now]:
        return

    if point_dic[now]:
        point = point_dic[now] + before
    else:
        point = before

    visited[now] = 1
    counter[now] += point

    for i in node[now]:
        if visited[i]:
            continue

        dfs(i, point)


dfs(1, 0)

print(' '.join(map(str, counter[1:])))
