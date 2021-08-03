from collections import defaultdict
from sys import setrecursionlimit  # 再帰エラー対策
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

# 各ノードの加算値を記録
for _ in range(q):
    p, x = map(int, input().split())
    point_dic[p] += x

# 現在のノード(now)とそれまでに加算された値(before_point)


def dfs(now, before_point):
    if visited[now]:
        return

    # 現在のノードの加算値を足す
    if point_dic[now]:
        point = point_dic[now] + before_point
    else:
        point = before_point

    # 訪問済みにする
    visited[now] = 1
    counter[now] += point

    for i in node[now]:
        if visited[i]:
            continue

        dfs(i, point)  # 再帰して子ノードに引き継ぐ


dfs(1, 0)

print(' '.join(map(str, counter[1:])))
