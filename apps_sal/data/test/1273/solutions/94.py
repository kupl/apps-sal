import sys
from collections import deque

n = int(input())
G = [[] for _ in range(n + 1)]
G_order = []
# a<bが保証されている、aを親、bを子とする
for i in range(n - 1):
    a, b = [int(x) - 1 for x in input().split()]
    G[a].append(b)
    G_order.append(b)

# どこでも良いが、ここでは0をrootとする
que = deque([0])

# 各頂点と「親」を結ぶ辺の色
# 頂点0をrootとするのでC[0]=0で確定, 他を調べる
colors = [0] * n

while que:
    # prt = 親
    # 幅優先探索
    prt = que.popleft()
    color = 0

    # cld = 子
    for cld in G[prt]:
        color += 1
        # 「今考えている頂点とその親を結ぶ辺の色」と同じ色は使えない
        if color == colors[prt]:
            color += 1
        colors[cld] = color
        que.append(cld)

# それぞれの頂点とその親を結ぶ辺の色
# print(colors)

# 必要な最小の色数
print((max(colors)))

# 辺の番号順に色を出力
for i in G_order:
    print((colors[i]))
