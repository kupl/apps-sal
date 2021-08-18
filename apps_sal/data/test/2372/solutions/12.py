
from collections import deque


def main():
    h, w = list(map(int, input().split()))
    ch, cw = list(map(int, input().split()))
    dh, dw = list(map(int, input().split()))

    """
    l = [list(input().strip()) for i in range(h)]
    ans = [[-1]*w for i in range(h)]
    for i in range(h):
        for j in range(w):
            if l[i][j] == "
                ans[i][j] = -2
    ch -= 1
    cw -= 1
    dh -= 1
    dw -= 1
    """

    base = ["
    base.append("
    for n in range(h):
        base.append("
    base.append("
    base.append("
    ans=[[-1] * (w + 4) for _ in range(h + 4)]
    for i in range(h + 4):
        for j in range(w + 4):
            if base[i][j] == "
                ans[i][j]=-2
    ch += 1
    cw += 1
    dh += 1
    dw += 1

    ans[ch][cw]=0
    move1=[[1, 0], [-1, 0], [0, 1], [0, -1]]
    move2=[
        [-2, -2], [-2, -1], [-2, 0], [-2, 1], [-2, 2], [-1, -2], [-1, -1],
        [-1, 1], [-1, 2], [0, -2], [0, 2], [1, -2], [1, -1], [1, 1],
        [1, 2], [2, -2], [2, -1], [2, 0], [2, 1], [2, 2]
    ]
    q1=deque([[ch, cw]])
    q2=deque([])

    while q1:
        x1, y1=q1.popleft()
        q2.append([x1, y1])
        for i, j in move1:
            nx, ny=x1 + i, y1 + j
            """
            if nx < 0 or h <= nx or ny < 0 or w <= ny:
                continue
            """
            if ans[nx][ny] == -1:
                ans[nx][ny]=ans[x1][y1]
                q1.append([nx, ny])
        if len(q1) == 0:
            while q2:
                x2, y2=q2.popleft()
                for i, j in move2:
                    mx, my=x2 + i, y2 + j
                    """
                    if mx < 0 or h <= mx or my < 0 or w <= my:
                        continue
                    """
                    if ans[mx][my] == -1:
                        ans[mx][my]=ans[x2][y2] + 1
                        q1.append([mx, my])
    print((ans[dh][dw]))


def __starting_point():
    main()


__starting_point()
