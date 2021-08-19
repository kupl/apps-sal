def prim_matrix(matrix: list, inf=10 ** 18):
    n = len(matrix)
    (costs, unused) = ([inf] * n, [0] + [1] * (n - 1))
    current = 0
    total_cost = 0
    nearest = [-1] * n
    (build, connect) = ([], [])
    for _ in range(n - 1):
        min_cost = inf
        dest = -1
        src = -1
        for i in range(n):
            if unused[i]:
                if matrix[current][i] < costs[i]:
                    costs[i] = matrix[current][i]
                    nearest[i] = current
                if min_cost > costs[i]:
                    min_cost = costs[i]
                    dest = i
                    src = nearest[i]
        total_cost += min_cost
        unused[dest] = 0
        if src == 0:
            build.append(dest)
        else:
            connect.append('%d %d' % (src, dest))
        current = dest
    print(total_cost)
    print(len(build))
    print(*build)
    print(len(connect))
    if connect:
        print(*connect, sep='\n')
    return total_cost


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
    cost = prim_matrix(matrix)


__starting_point()
