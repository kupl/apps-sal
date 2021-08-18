import sys
from collections import deque
input = sys.stdin.readline


def main():
    h, w = list(map(int, input().split()))
    ch, cw = list(map(int, input().split()))
    dh, dw = list(map(int, input().split()))

    ch += 1
    cw += 1
    dh += 1
    dw += 1

    s = ["
    s.append("
    for i in range(h):
        s.append("
    s.append("
    s.append("

    ans=[[-1] * (w + 4) for _ in range(h + 4)]
    for i in range(h + 4):
        for j in range(w + 4):
            if s[i][j] == "
                ans[i][j]=-2
    ans[ch][cw]=0

    move=[(-1, 0), (1, 0), (0, -1), (0, 1)]
    move2=[(-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2),
             (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2),
             (0, -2), (0, -1), (0, 0), (0, 1), (0, 2),
             (1, -2), (1, -1), (1, 0), (1, 1), (1, 2),
             (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)]

    not_yet=deque([(ch, cw)])
    one_time=deque([])

    while len(not_yet) > 0:
        x, y=not_yet.popleft()
        one_time.append((x, y))
        for (p, q) in move:
            v1, v2=x + p, y + q
            if ans[v1][v2] == -1:
                not_yet.append((v1, v2))
                ans[v1][v2]=ans[x][y]

        if len(not_yet) == 0:
            while len(one_time) > 0:
                x2, y2=one_time.popleft()
                for (v1, v2) in move2:
                    i, j=x2 + v1, y2 + v2
                    if ans[i][j] == -1:
                        ans[i][j]=ans[x2][y2] + 1
                        not_yet.append((i, j))

    print((ans[dh][dw]))


def __starting_point():
    main()


__starting_point()
