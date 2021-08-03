def resolve():
    from scipy.sparse.csgraph import shortest_path
    import scipy
    import numpy as numpy
    n, m = list(map(int, input().split()))
    row = [None] * m
    col = row[:]
    data = row[:]
    for i in range(m):
        row[i], col[i], data[i] = list(map(int, input().split()))
        row[i] -= 1
        col[i] -= 1
    a = scipy.sparse.csr_matrix((data, (row, col)), shape=(n, n)).toarray()
    s, p = shortest_path(a, return_predecessors=True, directed=False)
    l = [[True] * n for _ in range(n)]
    for start in range(n - 1):
        for goal in range(start + 1, n):
            path = get_path(start, goal, p)
            for i in range(len(path) - 1):
                l[path[i]][path[i + 1]] = False
                l[path[i + 1]][path[i]] = False
    ans = 0
    for i, j in zip(row, col):
        if l[i][j]:
            ans += 1
    print(ans)


def get_path(start, goal, pred):
    return get_path_row(start, goal, pred[start])


def get_path_row(start, goal, pred_row):
    path = []
    i = goal
    while i != start and i >= 0:
        path.append(i)
        i = pred_row[i]
    if i < 0:
        return []
    path.append(i)
    return path[::-1]


resolve()
