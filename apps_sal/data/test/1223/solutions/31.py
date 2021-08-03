import sys
import os
import math
3


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, P):
    revp = [-1] * (N + 1)
    for i, p in enumerate(P):
        revp[p] = i

    segt = [[(v, 0) for v in P]]
    while len(segt[-1]) > 1:
        base = segt[-1]
        if len(base) % 2 == 1:
            base.append((0, 0))
        new = []
        for i in range(len(base) // 2):
            a, b = base[2 * i]
            c, d = base[2 * i + 1]

            arr = [a, b, c, d]
            arr.sort()
            new.append((arr[-1], arr[-2]))
        segt.append(new)

    dprint('segt', segt)

    def get12(i, j):
        if j - i <= 0:
            return (0, 0)

        segi = 0
        top = []

        while True:
            if j - i <= 0:
                break

            seg = segt[segi]

            if j - i == 1:
                top.extend(seg[i])
                break

            if i % 2 == 1:
                top.extend(seg[i])
                i += 1
            if j % 2 == 1:
                top.extend(seg[j - 1])
                j -= 1

            i //= 2
            j //= 2
            segi += 1

        top.sort()
        return top[-1], top[-2]

    cache = [dict() for _ in range(N)]

    stk = [(0, N)]
    while stk:
        item = stk.pop()
        if len(item) == 2:
            i, j = item
            if j in cache[i]:
                continue

            a, b = get12(i, j)
            ai = revp[a]
            bi = revp[b]
            li, ri = (ai, bi) if ai < bi else (bi, ai)
            ri += 1

            sc = b * (li - i + 1) * (j - ri + 1)

            want = [(i, ri - 1), (li + 1, j), (li + 1, ri - 1)]
            req = []
            for c, d in want:
                if not (d - c < 2 or d in cache[c]):
                    req.append((c, d))
            if not req:
                left, right, mid = [0 if d - c < 2 else cache[c][d]
                                    for c, d in want]
                cache[i][j] = left + right - mid + sc
                continue

            stk.append((i, j, want, sc))
            for r in req:
                stk.append(r)
            continue

        i, j, want, sc = item
        left, right, mid = [0 if d - c < 2 else cache[c][d]
                            for c, d in want]
        cache[i][j] = left + right - mid + sc

    return cache[0][N]


def main():
    N = int(inp())
    P = [int(e) for e in inp().split()]
    print(solve(N, P))


def __starting_point():
    main()


__starting_point()
