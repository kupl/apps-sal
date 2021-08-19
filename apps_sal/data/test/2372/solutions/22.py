from collections import deque
from itertools import product


def main():
    h, w = list(map(int, input().split()))
    c = tuple([int(x) + 1 for x in input().split()])
    d = tuple([int(x) + 1 for x in input().split()])
    s = ['#' * (w + 4)] * 2 + [f'##{input()}##' for _ in range(h)] + ['#' * (w + 4)] * 2

    move_a_area = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    move_b_area = [(i, j) for i, j in product(list(range(-2, 3)), repeat=2) if (i, j) not in [(0, 0)] + move_a_area]

    cost = [[float('inf')] * (w + 4) for _ in range(h + 4)]
    cost[c[0]][c[1]] = 0
    yet = deque([(c[0], c[1], 0)])
    done = deque()

    while yet:
        y, x, m = yet.popleft()
        done.append((y, x, m))
        # Move A
        for dx, dy in move_a_area:
            hh, ww = y + dy, x + dx
            if s[hh][ww] == '#' or cost[hh][ww] <= m:
                continue
            cost[hh][ww] = m
            yet.append((hh, ww, m))
        # Move B
        if not yet:
            while done:
                y, x, m = done.popleft()
                for dx, dy in move_b_area:
                    hh, ww = y + dy, x + dx
                    if s[hh][ww] == '#' or cost[hh][ww] <= m + 1:
                        continue
                    cost[hh][ww] = m + 1
                    yet.append((hh, ww, m + 1))

    print((v if (v := cost[d[0]][d[1]]) < float('inf') else -1))


def __starting_point():
    main()


__starting_point()
