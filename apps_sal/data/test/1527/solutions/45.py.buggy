# ----------------
# ここから
# ----------------

import sys
from io import StringIO
import unittest
import copy
from collections import deque


def yn(b):
    print(("Yes" if b == 1 else "No"))
    return


def sagasu(h, w, mp, sh, sw):
    d = deque()
    x = sw
    y = sh
    d.append([y, x, 0])
    while len(d) > 0:
        y, x, cnt = d.popleft()
        if mp[y][x] == -2 or mp[y][x] > cnt:
            mp[y][x] = cnt
            nxt = [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]
            for nx in nxt:
                y2 = nx[0]
                x2 = nx[1]
                if y2 < 0:
                    continue
                if y2 >= h:
                    continue
                if x2 < 0:
                    continue
                if x2 >= w:
                    continue
                if mp[y2][x2] == -2 or mp[y2][x2] > cnt:
                    d.append([y2, x2, cnt + 1])
    ret = -1
    for y in range(h):
        for x in range(w):
            ret = max(ret, mp[y][x])
    return ret


def resolve():
    readline = sys.stdin.readline

    h, w = list(map(int, readline().rstrip().split()))

    mp = [[0 for i in range(w)] for j in range(h)]
    for y in range(h):
        ss = readline().rstrip()
        for x in range(w):
            if ss[x] == "#":
                mp[y][x] = -1  # kabe
            else:
                mp[y][x] = -2  # miti
    ans = 0
    for y in range(h):
        for x in range(w):
            if mp[y][x] == -2:
                mp2 = copy.deepcopy(mp)
                n = sagasu(h, w, mp2, y, x)
                ans = max(ans, n)
    print(ans)

    #arr=list(map(int, readline().rstrip().split()))
    # n=int(readline())
    # ss=readline().rstrip()
    # yn(1)

    return


if 'doTest' not in globals():
    resolve()
    return

# ----------------
# ここまで
# ----------------
