import sys
from collections import deque, Counter

def __starting_point():
    n, m, p = list(map(int, input().split()))
    speeds = list(map(int, input().split()))
    field = sys.stdin.readlines()

    lands = [-1] * (n * m)

    graph = [[] for _ in range(n * m)]

    starts = [deque() for _ in range(p)]

    levels = [-1] * n * m

    def calc(x, y): return x * m + y


    for i in range(n):
        for j in range(m):
            point = calc(i, j)
            if field[i][j].isdigit():
                player = int(field[i][j]) - 1
                starts[player].appendleft(point)
                lands[point] = player
                levels[point] = 0
            elif field[i][j] == '#':
                continue

            if 0 <= i - 1 and field[i - 1][j] == '.':
                graph[point].append(calc(i - 1, j))
            if i + 1 < n and field[i + 1][j] == '.':
                graph[point].append(calc(i + 1, j))
            if 0 <= j - 1 and field[i][j - 1] == '.':
                graph[point].append(calc(i, j - 1))
            if j + 1 < m and field[i][j + 1] == '.':
                graph[point].append(calc(i, j + 1))

    cnt = 0
    while [s for s in starts if s]:
        player = cnt % p
        turn = cnt // p + 1

        while starts[player]:
            if levels[starts[player][-1]] == speeds[player] * turn:
                break

            node = starts[player].pop()

            for nxt in graph[node]:
                if lands[nxt] != -1:
                    continue
                level = levels[node] + 1
                lands[nxt] = player
                levels[nxt] = levels[node] + 1
                starts[player].appendleft(nxt)

        cnt += 1

    cnt = list(Counter([l for l in lands if l != -1]).items())
    cnt.sort()

    print(" ".join([str(x[1]) for x in cnt]))



__starting_point()
