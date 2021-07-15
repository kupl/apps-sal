import queue


def bfs01(s: int, t: int, V: int, graph: list)->int:
    '''01-bfs
    :param s: source
    :param t: sink
    :param V: number of vertex
    :param graph: graph
    :return: minimum distance from `s` to `t`
    '''
    INF = float('inf')

    # deque と s から各頂点への距離を初期化する。
    q = queue.deque([])  # deque
    qc = 0               # 毎度 len(q) を回すと時間かかりそうなので変数で管理
    l = [INF] * V        # s から各頂点への距離

    # s に関する初期化
    q.append(s)
    qc += 1
    l[s] = 0

    # deque に頂点が存在する限り次を繰り返す。
    # 1. deque の先頭から頂点を取り出す。
    # 2. 取り出した頂点に隣接する全ての頂点に対して以下を行う。
    # 2-a. 距離が更新されるなら更新する。加えて辺の長さが 0 なら
    #      先頭に、1 なら末尾に追加する。
    while qc > 0:
        u = q.popleft()
        qc -= 1
        for v, c in graph[u]:
            if l[u] + c < l[v]:
                l[v] = l[u] + c
                qc += 1
                if c == 0:
                    q.appendleft(v)
                else:
                    q.append(v)

    return l[t]


def small_multiple(K: int)->int:
    graph = []
    for k in range(K):
        # k -> k+1 に 1 の辺を、k -> 10*k に 0 の辺を張る。
        # ただし、どちらも mod K をとって k と等しくない場合のみ
        graph.append([])
        v1 = k+1 if k+1 < K else 0
        v10 = (k*10) % K

        graph[k].append((v1, 1))
        if v10 != k:
            graph[k].append((v10, 0))

    return bfs01(1, 0, K, graph) + 1


def __starting_point():
    K = int(input())
    ans = small_multiple(K)
    print(ans)

__starting_point()
