from collections import deque

n = int(input())

g = [[] for _ in range(n)]
# 0indexに直している
for i in range(n - 1):
    u, v, w = list(map(int, input().split()))
    g[u - 1].append((v - 1, w))
    g[v - 1].append((u - 1, w))

"""
ex.
3
1 2 2
2 3 1
の場合、g = [[(1, 2)], [(0, 2), (2, 1)], [(1, 1)]]
"""

#print(g)

"""
根から各頂点への距離をd_iとする
u,vという2頂点について、その最小共通祖先をwとすると
uとvの距離=d_u+d_v-2d_w
第3項は常に偶数
d_uとd_vの偶奇が等しければ全体は偶数、偶奇が異なれば全体は奇数
例えば、d_iが偶数なら白に、奇数なら黒に塗るとすれば条件を満たす
"""

dq = deque([0])
#  各頂点について、根からの距離
# 頂点0を根とする（別にどれを選んでも良い）
ds = [-1] * n
ds[0] = 0

# BFS(幅優先探索)
while dq:
    t = dq.popleft()
    # tと繋がっている各頂点について
    for i in g[t]:
        # まだ調べていない場合
        if ds[i[0]] == -1:
            # 根からtまでの距離+tから次への距離
            ds[i[0]] = ds[t] + i[1]
            # 今調べた頂点をdequeに追加
            dq.append((i[0]))

# 偶数なら白、奇数なら黒とした。逆でも良い。
for i in ds:
    if i % 2 == 0:
        print((0))
    else:
        print((1))

