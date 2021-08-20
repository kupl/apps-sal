import time


def get_frontiers(feild, n, m, p):
    frontiers = [[] for i in range(p)]
    for i in range(n):
        for j in range(m):
            ele = feild[i][j]
            if 1 <= ele <= 9:
                frontiers[ele - 1].append((i, j))
    return frontiers


def go(player_id, frontier, n_turn, feild, n, m):
    frontier = frontier
    while n_turn and frontier:
        n_turn -= 1
        new_frontier = []
        for (i, j) in frontier:
            if i + 1 < n:
                new_space = feild[i + 1][j]
                if not new_space:
                    feild[i + 1][j] = player_id
                    new_frontier.append((i + 1, j))
            if i - 1 >= 0:
                new_space = feild[i - 1][j]
                if not new_space:
                    feild[i - 1][j] = player_id
                    new_frontier.append((i - 1, j))
            if j + 1 < m:
                new_space = feild[i][j + 1]
                if not new_space:
                    feild[i][j + 1] = player_id
                    new_frontier.append((i, j + 1))
            if j - 1 >= 0:
                new_space = feild[i][j - 1]
                if not new_space:
                    feild[i][j - 1] = player_id
                    new_frontier.append((i, j - 1))
        frontier = new_frontier
    return frontier


def solve(speeds, feild, n, m, p):
    frontiers = get_frontiers(feild, n, m, p)
    hope = set(range(p))
    while hope:
        new_hope = set()
        for i in hope:
            n_turn = speeds[i]
            frontier = frontiers[i]
            new_frontier = go(i + 1, frontier, n_turn, feild, n, m)
            if new_frontier:
                new_hope.add(i)
            frontiers[i] = new_frontier
        hope = new_hope
    result = get_frontiers(feild, n, m, p)
    return [len(ele) for ele in result]


def test():
    (n, m, p) = (1000, 1000, 9)
    speeds = [1000000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 1]
    feild = [[0, -1] * (m // 2) for i in range(n)]
    for i in range(m):
        if i % 4 != 1:
            feild[0][i] = 0
        if i % 4 != 3:
            feild[n - 1][i] = 0
    for i in range(9):
        feild[0][i * 8] = i + 1
    tick = time.time()
    result = solve(speeds, feild, n, m, p)
    tock = time.time()
    print(' '.join(map(str, result)))
    print('T:', round(tock - tick, 5))


def main():
    d = {str(i): i for i in range(1, 10)}
    d['.'] = 0
    d['#'] = -1
    (n, m, p) = map(int, input().split())
    speeds = list(map(int, input().split()))
    feild = []
    for i in range(n):
        feild.append(list(map(d.get, input())))
    result = solve(speeds, feild, n, m, p)
    print(' '.join(map(str, result)))


def __starting_point():
    main()


__starting_point()
