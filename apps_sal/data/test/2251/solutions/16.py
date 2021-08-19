def get_connected_matrix(adjacency_matrix):
    n = len(adjacency_matrix)
    non_visited_vertices = set((i for i in range(n)))
    cluster_numbers = [0] * n
    cluster_number = 1

    def traverse(u):
        non_visited_vertices.remove(u)
        cluster_numbers[u] = cluster_number
        for v in range(n):
            if v in non_visited_vertices:
                if adjacency_matrix[u][v]:
                    traverse(v)
    while non_visited_vertices:
        vertex = non_visited_vertices.pop()
        non_visited_vertices.add(vertex)
        traverse(vertex)
        cluster_number += 1
    connected_matrix = [[False] * n for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            connected_matrix[u][v] = connected_matrix[v][u] = cluster_numbers[u] == cluster_numbers[v]
    return connected_matrix


def main():
    (n, m) = [int(t) for t in input().split()]
    matrices = [[[False] * n for _ in range(n)] for _ in range(m)]
    for _ in range(m):
        (a, b, c) = [int(t) - 1 for t in input().split()]
        matrices[c][a][b] = True
        matrices[c][b][a] = True
    connected_matrices = [get_connected_matrix(matrix) for matrix in matrices]
    q = int(input())
    for _ in range(q):
        (u, v) = [int(t) - 1 for t in input().split()]
        total_connection = sum((1 for connected_matrix in connected_matrices if connected_matrix[u][v]))
        print(total_connection)


def __starting_point():
    main()


__starting_point()
