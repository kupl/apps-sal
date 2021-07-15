# 解説と提出#12551970を参考に作成
# 今いる都市と銀貨の所持数を状態として、
#   ①その都市から移動可能な別の都市に移動する
#   ②金貨を銀貨に交換する
# のどちらかを行い、実施後の(同都市・同所持銀貨枚数での)最小時間を計測していく。
# 最小時間が更新された場合、さらにその状態から①・②を行う。
# これによって全都市・全銀貨所持枚数毎の最小時間を割り出す。
# 都市の銀貨所持枚数毎の最小時間の中での最小時間がその都市へ行くための最小時間になる。
#   ※1: 都市への移動は移動可能な枚数の銀貨を持っている場合のみ可能
#   ※2: 銀貨の最大所持枚数は (N - 1) * max(Ai) とする
#        -> 一番遠い都市に移動する場合にかかりうる最大の銀貨枚数

from heapq import heappop, heappush


def solve():
    n, m, s = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    # グラフ作製
    max_a = 0
    for _ in range(m):
        u, v, a, b = list(map(int, input().split()))
        graph[u - 1].append([v - 1, a, b])
        graph[v - 1].append([u - 1, a, b])
        max_a = max(max_a, a)
    ce = [[int(i) for i in input().split()] for _ in range(n)]
    # 初期値マップ作製
    maxSilver = max_a * (n - 1)  # max(a) * (n - 1)
    inf = float('inf')
    ns_map = [[inf] * (maxSilver + 1) for _ in range(n)]
    # スタート時の値設定と探索
    q = [[0, 0, min(maxSilver, s)]]  # 累計時間, 都市, 所持銀貨
    ns_map[0][min(maxSilver, s)] = 0  # スタート地点の時刻は0
    while q:
        ti, ni, si = heappop(q)
        # 移動
        for g in graph[ni]:
            n2, ai, bi = g
            if si >= ai and ns_map[n2][si - ai] > ti + bi:
                ns_map[n2][si - ai] = ti + bi
                # ★heapq で累計時間が少ない情報から先に処理するようにする.
                # これによって処理速度が全然違う
                heappush(q, [ti + bi, n2, si - ai])
        # 換金
        ci, di = ce[ni]
        ti += di
        si = min(si + ci, maxSilver)
        if ns_map[ni][si] > ti:
            ns_map[ni][si] = ti
            heappush(q, [ti, ni, si])
    for i in range(1, n):
        print((min(ns_map[i])))


def __starting_point():
    solve()

__starting_point()
