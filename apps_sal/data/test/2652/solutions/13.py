# built
# x軸の昇順で並べたリスト、y軸の昇順で並べたリストを作る。
# どちらかのリストで隣にある点同士を辺でむすぶ。
# 最小全域木

import heapq as hq
import sys
readline = sys.stdin.readline

N = int(readline())
point = [None] * N
for i in range(N):
    point[i] = list(map(int, readline().split())) + [i]

X = sorted(point, key=lambda x: x[0])
Y = sorted(point, key=lambda x: x[1])

G = [[] for i in range(N)]

for i in range(len(X) - 1):
    x1, y1, ind_1 = X[i]
    x2, y2, ind_2 = X[i + 1]
    G[ind_1].append([ind_2, min(abs(x1 - x2), abs(y1 - y2))])
    G[ind_2].append([ind_1, min(abs(x1 - x2), abs(y1 - y2))])

for i in range(len(Y) - 1):
    x1, y1, ind_1 = Y[i]
    x2, y2, ind_2 = Y[i + 1]
    G[ind_1].append([ind_2, min(abs(x1 - x2), abs(y1 - y2))])
    G[ind_2].append([ind_1, min(abs(x1 - x2), abs(y1 - y2))])

# 進むことができる頂点のうち、最もコストが小さいものを採用する
# heapqで、次に行くことができる(コスト, 頂点)を管理
# 頂点が追加されたら、そこから進むことができる頂点を全てheapqに追加する
# 訪問済み頂点はsetで管理することで除外
# 全てが訪問済みになったら（heapqが空になったら）終了

q = [(0, 0)]
hq.heapify(q)
visited = set()

ans = 0
while q:
    cost, v = hq.heappop(q)
    if v in visited:
        continue
    visited.add(v)
    ans += cost
    for child in G[v]:
        if child[0] in visited:
            continue
        hq.heappush(q, (child[1], child[0]))

print(ans)
