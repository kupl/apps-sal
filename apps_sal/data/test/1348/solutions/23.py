

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    n, k = read_ints()
    d = read_ints()
    S = [[] for _ in range(n)]
    for i in range(n):
        S[d[i]].append(i)
    if len(S[0]) != 1:
        return -1
    G = [[] for _ in range(n)]
    degree = [0] * n
    depth = 1
    construct_count = 1
    edges = []
    for depth in range(1, n):
        i = 0
        prev_len = len(S[depth - 1])
        if len(S[depth]) == 0:
            break
        for vertex in S[depth]:
            parent_vertex = S[depth - 1][i % prev_len]
            degree[parent_vertex] += 1
            if degree[parent_vertex] > k:
                return -1
            degree[vertex] += 1
            if degree[vertex] > k:
                return -1
            G[parent_vertex].append(vertex)
            edges.append((parent_vertex, vertex))
            construct_count += 1
            i += 1
    if construct_count != n:
        return -1
    print(len(edges))
    for u, v in edges:
        print(u + 1, v + 1)


def __starting_point():
    if solve() == -1:
        print(-1)


__starting_point()
