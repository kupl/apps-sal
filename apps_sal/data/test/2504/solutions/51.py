import numpy as np
from scipy.sparse.csgraph import shortest_path
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import csgraph_from_dense

INF = float('inf')

def main():
    N, M, L = map(int, input().split())

    # G[x][y]: xからyへ直接移動するときのコスト。移動できない場合はINF
    G = [[INF] * (N+1) for n in range(N+1)]

    for i in range(M):
        a, b, c = map(int, input().split())
        G[a][b] = c
        G[b][a] = c
    G = csgraph_from_dense(G, null_value=INF)

    Q = int(input())
    Queries = []
    for i in range(Q):
        s, t = map(int, input().split())
        Queries.append((s, t))

    # ワーシャルフロイド法で、全点間の距離を求める
    cost = floyd_warshall(G)
    # 全点間の距離のうち、移動距離がL以内でおさまる頂点同士は、給油せずにすむ
    # そこで、全点間の距離のうち、移動距離がL以内でおさまる頂点同士を距離1で結んだグラフを作成し、
    # そのグラフに対してワーシャルフロイド法で最短距離を計算することで、
    # refuel[x][y] =「xからyへ移動するときの給油回数+1」というグラフを作成できる
    no_refuel = [[1 if x <= L else INF for x in c] for c in cost]
    no_refuel = csgraph_from_dense(no_refuel, null_value=INF)
    refuel_count = floyd_warshall(no_refuel)

    ans = []
    for s, t in Queries:
        d = refuel_count[s][t]
        ans.append(int(d-1) if d != INF else -1)
    
    print(*ans, sep='\n')

def __starting_point():
    main()
__starting_point()
