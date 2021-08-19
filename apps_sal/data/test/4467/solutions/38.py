def c_2d_plane_2n_points_bipartite_graph():
    import networkx as nx
    from networkx.algorithms.flow import dinitz
    N = int(input())
    Red_point_pos = [[int(i) for i in input().split()] for j in range(N)]
    Blue_point_pos = [[int(i) for i in input().split()] for j in range(N)]
    graph = nx.DiGraph()
    graph.add_nodes_from(range(2 * N + 2))
    for i in range(N):
        for j in range(N):
            (a, b) = Red_point_pos[i]
            (c, d) = Blue_point_pos[j]
            if a < c and b < d:
                graph.add_edge(i + 1, j + N + 1, capacity=1)
    for i in range(1, N + 1):
        graph.add_edge(0, i, capacity=1)
    for j in range(N + 1, 2 * N + 1):
        graph.add_edge(j, 2 * N + 1, capacity=1)
    return dinitz(graph, 0, 2 * N + 1).graph['flow_value']


print(c_2d_plane_2n_points_bipartite_graph())
