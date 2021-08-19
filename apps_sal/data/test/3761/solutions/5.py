
from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def solve():
    S = input()[:-1]
    GX, GY = list(map(int, input().split()))

    # 連続するFをまとめる ex.)FF->2
    # 連続するTをまとめる ex.)TTT->T
    S_parsed = []
    prev = S[0]
    seq = 1
    for c in S[1:]:
        if c == "F":
            if c == prev:
                seq += 1
            else:
                prev = c
                if seq % 2 == 0:
                    pass
                else:
                    S_parsed.append("T")
                seq = 1
        elif c == "T":
            if c == prev:
                seq += 1
            else:
                S_parsed.append(seq)
                seq = 1
            prev = c
    else:
        if S[-1] == "F":
            S_parsed.append(seq)

    # x,yを分離して考える
    x_move = []
    y_move = []

    dir_x = True
    for c in S_parsed:
        if c == "T":
            dir_x = not dir_x
        else:
            if dir_x:
                x_move.append(c)
            else:
                y_move.append(c)

    # x,y分けて、GX,GYに到達できるかをdpで判定
    dp_x = defaultdict(bool)
    if len(x_move) > 0:
        if S[0] != "T":
            dp_x[x_move[0]] = True
        else:
            dp_x[x_move[0]] = True
            dp_x[-x_move[0]] = True
    else:
        dp_x[0] = True

    for x in x_move[1:]:
        tmp = defaultdict(bool)
        for key, val in list(dp_x.items()):
            tmp[key + x] = True
            tmp[key - x] = True
        dp_x = tmp

    dp_y = defaultdict(bool)
    if len(y_move) == 0:
        dp_y[0] = True
    else:
        dp_y[y_move[0]] = True
        dp_y[-y_move[0]] = True
    for y in y_move[1:]:
        tmp = defaultdict(bool)
        for key, val in list(dp_y.items()):
            tmp[key + y] = True
            tmp[key - y] = True
        dp_y = tmp

    if dp_x[GX] and dp_y[GY]:
        print("Yes")
    else:
        print("No")


solve()
