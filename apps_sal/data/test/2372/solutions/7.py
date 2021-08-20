from collections import deque


def main():
    (h, w) = map(int, input().split())
    (ch, cw) = map(int, input().split())
    (dh, dw) = map(int, input().split())
    base = ['#' * (w + 4)]
    base.append('#' * (w + 4))
    for n in range(h):
        base.append('##' + input() + '##')
    base.append('#' * (w + 4))
    base.append('#' * (w + 4))
    ans = [[-1] * (w + 4) for _ in range(h + 4)]
    for j in range(w + 4):
        for i in range(h + 4):
            if base[i][j] == '#':
                ans[i][j] = -2
    ch += 1
    cw += 1
    dh += 1
    dw += 1
    ans[ch][cw] = 0
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    move2 = [[-2, -2], [-2, -1], [-2, 0], [-2, 1], [-2, 2], [-1, -2], [-1, -1], [-1, 0], [-1, 1], [-1, 2], [0, -2], [0, -1], [0, 0], [0, 1], [0, 2], [1, -2], [1, -1], [1, 0], [1, 1], [1, 2], [2, -2], [2, -1], [2, 0], [2, 1], [2, 2]]
    q = deque([[ch, cw]])
    one_time = deque([])
    while len(q) > 0:
        (x, y) = q.popleft()
        one_time.append([x, y])
        for (i, j) in move:
            (v1, v2) = (x + i, y + j)
            if ans[v1][v2] == -1:
                ans[v1][v2] = ans[x][y]
                q.append([v1, v2])
        if len(q) == 0:
            while len(one_time) > 0:
                (x2, y2) = one_time.popleft()
                for (i, j) in move2:
                    (v1, v2) = (x2 + i, y2 + j)
                    if ans[v1][v2] == -1:
                        ans[v1][v2] = ans[x2][y2] + 1
                        q.append([v1, v2])
    print(ans[dh][dw])


def __starting_point():
    main()


__starting_point()
