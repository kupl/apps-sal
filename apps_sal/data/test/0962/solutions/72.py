import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from collections import deque


def find_shortest_cycle(G, s):
    dq = deque()
    N = len(G)
    INF = float('inf')
    dist = [INF] * N
    dist[s] = 0
    parent = [-1] * N

    ans_last = None # sからループを探して見つかった時の、ループの最後の頂点番号
    dq.append(s)
    # BFSで、最短のループを見つける
    while dq and ans_last is None:
        v = dq.popleft()
        d = dist[v]
        for n in G[v]:
            # 頂点vからいける頂点の中に開始点があったら、ループである
            if dist[n] == 0:
                ans_last = v
                parent[n] = v
                break
            # まだ探索していない頂点なら次の探索候補にする
            elif dist[n] == INF:
                dist[n] = d + 1
                parent[n] = v
                dq.append(n)

    # ループが見つかった場合
    if ans_last:
        # ループの最後の頂点から、元の頂点をたどり、そのルートを逆にする
        g = ans_last
        route = [g]
        while g != s:
            g = parent[g]
            route.append(g)
        return list(reversed(route))
    
    # 見つからなかった場合はNoneを返す
    return None

def main():
    N, M, *A = map(int, read().split())

    G = [[] for i in range(N+1)]
    for a, b in zip(A[::2], A[1::2]):
        G[a].append(b)

    # すべての頂点の入次数が 1、出次数が 1 であるような G の誘導部分グラフ
    # [すべての頂点の入次数が 1、出次数が 1 のグラフ] -> ループ

    # 有向グラフ G=(V,E) に対し、次のような条件を満たす有向グラフ G′=(V′,E′) を G の誘導部分グラフと呼ぶ。
    # V′ は V の (空でない) 部分集合である。
    # E′ は、E の辺であって両端点がともに V′ に含まれるものすべてを含む集合である。

    # -> ループでも、ショートカットできるようなループはだめ

    # 例: 1 -> 2 -> 3 -> 4 -> 5
    #     ^    |         ^    |
    #     |    ----------|    |
    #     ---------------------
    # V' = {1, 2, 3, 4, 5} としてしまうと、
    # E' = {(1->2), (2->3), (3->4), (2->4), (4->5), (5->1)}
    # となってしまい、この誘導部分グラフG'=(V', E')において、
    # 頂点2の出次数が2になってしまう。（頂点4の入次数も2になってしまう）
    # V' = {1, 2, 4, 5} とすれば、
    # E' = {(1->2), (2->4), (4->5), (5->1)}
    # となり、すべての頂点の入次数が 1、出次数が 1 となる
    
    # つまり、ショートカットできない最短のループを1つでも見つければよい
    
    min_route = None
    for s in range(1, N+1):
        # 各頂点を開始点にしてループを探す
        route = find_shortest_cycle(G, s)
        # ループが複数ある場合、短いほうを採用
        if route:
            if min_route is None or len(route) < len(min_route):
                min_route = route
    
    if min_route:
        print(len(min_route), *min_route, sep='\n')
    else:
        print(-1)

def __starting_point():
    main()
__starting_point()
