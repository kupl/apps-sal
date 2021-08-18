# 幅優先探索で連結成分を求めるプログラム
from collections import deque

# n = int(input())# ノードの数
n, m = map(int, input().split())

l = [list(map(int, input().split())) for _ in range(m)]

ans = 0


def bfs(start_node, color_id):  # start_nodeは探索の開始点
    nonlocal color, d
    q = deque([start_node])
    d[start_node] = 0
    color[start_node] = color_id
    while len(q) != 0:
        u = q.popleft()
        for v in adjl[u]:
            if color[v] == NIL:
                d[v] = d[u] + 1
                color[v] = color_id
                q.append(v)


# print(l)
for k in range(1, m + 1):

    # 隣接リストで格納する
    adjl = [[] for _ in range(n + 1)]
    for i in range(1, m + 1):  # 隣接関係を受け取る
        if i == k:
            continue
        s, t = l[i - 1]
        adjl[s].append(t)
        adjl[t].append(s)

    NIL = -1  # 未発見を示す値
    d = [-1 for i in range(n + 1)]  # 頂点1からの距離を格納するリスト
    color = [NIL for i in range(n + 1)]  # 未到達かを示すリスト

    # print(adjl)

    color_id = 0
    for u in range(1, n + 1):  # node全てからスタートする
        if color[u] == NIL:
            color_id += 1
            bfs(u, color_id)

    # print(color)
    if len(set(color)) >= 3:
        ans += 1
print(ans)
