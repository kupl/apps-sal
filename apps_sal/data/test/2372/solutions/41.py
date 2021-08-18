from collections import *


def main():
    H, W = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    s = ["
    s.append("
    for i in range(H):
        s.append("
    s.append("
    s.append("

    ans=[[-1] * (W + 4) for _ in range(H + 4)]
    for i in range(H + 4):
        for j in range(W + 4):
            if s[i][j] == "
                ans[i][j]=-2
    ch += 1
    cw += 1
    dh += 1
    dw += 1
    ans[ch][cw]=0

    move=[[-1, 0], [1, 0], [0, -1], [0, 1]]
    magic=[
        [-2, -2], [-2, -1], [-2, 0], [-2, 1], [-2, 2],
        [-1, -2], [-1, -1], [-1, 0], [-1, 1], [-1, 2],
        [0, -2], [0, -1], [0, 0], [0, 1], [0, 2],
        [1, -2], [1, -1], [1, 0], [1, 1], [1, 2],
        [2, -2], [2, -1], [2, 0], [2, 1], [2, 2]
    ]

    mylist=deque([[ch, cw]])
    mylist2=deque([])
    while len(mylist) > 0:
        x, y=mylist.popleft()
        mylist2.append([x, y])
        for p, q in move:
            v1, v2=x + p, y + q
            if ans[v1][v2] == -1:
                mylist.append([v1, v2])
                ans[v1][v2]=ans[x][y]
        if len(mylist) == 0:
            while len(mylist2) > 0:
                x2, y2=mylist2.popleft()
                for v1, v2 in magic:
                    i, j=x2 + v1, y2 + v2
                    if ans[i][j] == -1:
                        ans[i][j]=ans[x2][y2] + 1
                        mylist.append([i, j])
    print(ans[dh][dw])


def __starting_point():
    main()


__starting_point()
