def f_pure():
    # 参考: http://drken1215.hatenablog.com/entry/2019/09/29/012000
    from collections import deque
    N, M = [int(i) for i in input().split()]

    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = [int(i) for i in input().split()]
        graph[a - 1].append(b - 1)

    shortest = N + 1
    ans = []
    for s in range(N):
        # 頂点sから他の辺へ行くには何個の頂点を辿る必要があるか計算する
        dist = [-1] * N
        previous = [-1] * N  # [n]: 頂点nへはどこから来たか
        queue = deque([s])
        dist[s] = 0
        while queue:
            v = queue.pop()
            for next_node in graph[v]:
                if dist[next_node] == -1:
                    dist[next_node] = dist[v] + 1
                    previous[next_node] = v
                    queue.appendleft(next_node)

        for t in range(N):
            if t == s or dist[t] == -1:
                continue  # 頂点tは始点と同じ、または、始点から到達不可能
            for next_node in graph[t]:
                if next_node == s:  # ループ完成
                    ans_tmp = [s]  # 解になりうる頂点集合
                    current_node = t
                    # 頂点tからsまで巻き戻していく
                    while current_node != s:
                        ans_tmp.append(current_node)
                        current_node = previous[current_node]
                    # 頂点集合の濃度が減少した
                    if shortest > len(ans_tmp):
                        shortest = len(ans_tmp)
                        ans = ans_tmp

    if shortest == N + 1:
        return -1  # 閉路がなかった。条件を満たす頂点集合はない
    return ' '.join(map(str, [len(ans)] + sorted(v + 1 for v in ans)))

print(f_pure())
