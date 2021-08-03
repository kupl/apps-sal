__author__ = 'MoonBall'

import sys
# sys.stdin = open('data/B.in', 'r')
T = 1


def process():
    x, y, x0, y0 = list(map(int, input().split()))
    s = input()
    d = {}
    L = len(s)

    cnt = [0] * (L + 1)
    d[x0] = {}
    d[x0][y0] = 0

    for idx, _s in enumerate(s):
        if _s == 'L':
            y0 = max(1, y0 - 1)
        elif _s == 'R':
            y0 = min(y, y0 + 1)
        elif _s == 'U':
            x0 = max(1, x0 - 1)
        elif _s == 'D':
            x0 = min(x, x0 + 1)

        if not d.get(x0):
            d[x0] = {}
        t = d[x0]
        if t.get(y0) == None:
            t[y0] = idx + 1

    for i, _ in list(d.items()):
        for j, v in list(_.items()):
            cnt[v] = cnt[v] + 1

    cnt[L] = cnt[L] + x * y - sum(cnt)
    print(' '.join(map(str, cnt[0:L + 1])))


for _ in range(T):
    process()
