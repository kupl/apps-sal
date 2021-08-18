def f_pure():
    from collections import deque
    N, M = [int(i) for i in input().split()]

    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = [int(i) for i in input().split()]
        graph[a - 1].append(b - 1)

    shortest = N + 1
    ans = []
    for s in range(N):
        dist = [-1] * N
        previous = [-1] * N
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
                continue
            for next_node in graph[t]:
                if next_node == s:
                    ans_tmp = [s]
                    current_node = t
                    while current_node != s:
                        ans_tmp.append(current_node)
                        current_node = previous[current_node]
                    if shortest > len(ans_tmp):
                        shortest = len(ans_tmp)
                        ans = ans_tmp

    if shortest == N + 1:
        return -1
    return ' '.join(map(str, [len(ans)] + sorted(v + 1 for v in ans)))


print(f_pure())
