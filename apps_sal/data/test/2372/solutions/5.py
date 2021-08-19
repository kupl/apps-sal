from collections import deque


def main():
    (h, w) = list(map(int, input().split()))
    (start_h, start_w) = [int(x) + 1 for x in input().split()]
    (goal_h, goal_w) = [int(x) + 1 for x in input().split()]
    s = ['#' * (w + 4)]
    s.append('#' * (w + 4))
    for _ in range(h):
        s.append('##' + input() + '##')
    s.append('#' * (w + 4))
    s.append('#' * (w + 4))
    ans = [[-1] * (w + 4) for _ in range(h + 4)]
    for i in range(h + 4):
        for j in range(w + 4):
            if s[i][j] == '#':
                ans[i][j] = -2
    ans[start_h][start_w] = 0
    move1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    move2 = [(-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, -2), (0, -1), (0, 0), (0, 1), (0, 2), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)]
    yet = deque([(start_h, start_w)])
    done = deque()
    while yet:
        (x1, y1) = yet.popleft()
        done.append((x1, y1))
        for (p, q) in move1:
            (v1, v2) = (x1 + p, y1 + q)
            if ans[v1][v2] == -1:
                yet.append((v1, v2))
                ans[v1][v2] = ans[x1][y1]
        if len(yet) == 0:
            while done:
                (x2, y2) = done.popleft()
                for (p, q) in move2:
                    (i, j) = (x2 + p, y2 + q)
                    if ans[i][j] == -1:
                        ans[i][j] = ans[x2][y2] + 1
                        yet.append((i, j))
    print(ans[goal_h][goal_w])


def __starting_point():
    main()


__starting_point()
