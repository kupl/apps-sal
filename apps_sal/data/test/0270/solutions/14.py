def f_fork_in_the_road():
    (N, M) = [int(i) for i in input().split()]
    Nodes = [[int(i) for i in input().split()] for j in range(M)]
    edges = [[] for _ in range(N)]
    for (s, t) in Nodes:
        edges[s - 1].append(t - 1)
    probability = [0] * N
    probability[0] = 1.0
    for v in range(N):
        for next_vertex in edges[v]:
            probability[next_vertex] += probability[v] / len(edges[v])
    expected_value = [0] * N
    for v in range(N - 2, -1, -1):
        for next_vertex in edges[v]:
            expected_value[v] += expected_value[next_vertex]
        expected_value[v] = 1 + expected_value[v] / len(edges[v])
    ans = expected_value[0]
    for v in range(N):
        if len(edges[v]) <= 1:
            continue
        v_max_expected = max(((expected_value[w], w) for w in edges[v]))[1]
        expected_diff = 0.0
        outdegree = len(edges[v])
        for next_vertex in edges[v]:
            if next_vertex == v_max_expected:
                expected_diff -= expected_value[next_vertex] / outdegree
            else:
                expected_diff += expected_value[next_vertex] / (outdegree * (outdegree - 1))
        ans = min(ans, expected_value[0] + probability[v] * expected_diff)
    return round(ans, 10)


print(f_fork_in_the_road())
