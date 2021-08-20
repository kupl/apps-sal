def prim(matrix, inf=10 ** 18):
    n = len(matrix)
    costs = [inf] + [inf - 1] * (n - 1)
    nearest = [-1] * n
    current = 0
    total_cost = 0
    (build, connect) = ([], [])
    for _ in range(n - 1):
        min_cost = inf
        (src, dest) = (-1, -1)
        for i in range(n):
            if costs[i] == inf:
                continue
            if matrix[current][i] < costs[i]:
                costs[i] = matrix[current][i]
                nearest[i] = current
            if min_cost > costs[i]:
                min_cost = costs[i]
                (src, dest) = (nearest[i], i)
        total_cost += min_cost
        costs[dest] = inf
        if src == 0:
            build.append(dest)
        else:
            connect.append('%d %d' % (src, dest))
        current = dest
    return (build, connect, total_cost)


def __starting_point():
    import sys
    n = int(input())
    pos = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    c_costs = list(map(int, input().split()))
    k_costs = list(map(int, input().split()))
    inf = 10 ** 18
    matrix = [[inf] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i + 1][j + 1] = matrix[j + 1][i + 1] = (abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1])) * (k_costs[i] + k_costs[j])
        matrix[i + 1][0] = matrix[0][i + 1] = c_costs[i]
    (build, connect, cost) = prim(matrix)
    print(cost)
    print(len(build))
    print(*build)
    print(len(connect))
    if connect:
        print(*connect, sep='\n')


__starting_point()
