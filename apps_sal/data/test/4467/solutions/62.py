def c_2d_plane_2n_points_bipartite_graph():
    import networkx as nx
    from networkx.algorithms.flow import dinitz
    N = int(input())
    (A, B, C, D) = ([], [], [], [])
    for _ in range(N):
        (a, b) = [int(i) for i in input().split()]
        A.append(a)
        B.append(b)
    for _ in range(N):
        (c, d) = [int(i) for i in input().split()]
        C.append(c)
        D.append(d)
    graph = nx.DiGraph()
    graph.add_nodes_from(range(2 * N + 2))
    for i in range(N):
        for j in range(N):
            if A[i] < C[j] and B[i] < D[j]:
                graph.add_edge(i + 1, j + N + 1, capacity=1)
    for i in range(1, N + 1):
        graph.add_edge(0, i, capacity=1)
    for j in range(N + 1, 2 * N + 1):
        graph.add_edge(j, 2 * N + 1, capacity=1)
    return dinitz(graph, 0, 2 * N + 1).graph['flow_value']


print(c_2d_plane_2n_points_bipartite_graph())
