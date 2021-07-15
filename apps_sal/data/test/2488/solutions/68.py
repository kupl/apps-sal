import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, d, a = list(map(int, input().split()))
    XH = sorted([list(map(int, input().split())) for _ in range(n)])

    res = 0
    tt_dmg = 0
    que = deque()
    for x, h in XH:
        while que and que[0][1] < x:
            dmg, rng = que.popleft()
            tt_dmg -= dmg

        if tt_dmg < h:
            h -= tt_dmg
            cnt = (h + a - 1) // a
            res += cnt
            dmg = cnt * a
            tt_dmg += dmg
            que.append((dmg, x + d * 2))

    print(res)


def __starting_point():
    resolve()

__starting_point()
