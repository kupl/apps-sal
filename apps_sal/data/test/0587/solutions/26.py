#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, K: int, t: "List[int]", d: "List[int]"):
    ss = sorted(zip(d, t), reverse=True)
    gs = []
    mst = set()
    for di, ti in ss[:K]:
        if ti in mst:
            gs.append((di, ti))
        else:
            mst.add(ti)
    dm = {}
    for di, ti in ss[K:]:
        if ti in dm or ti in mst:
            continue
        dm[ti] = di
    hs = sorted(((di, ti) for ti, di in list(dm.items())), reverse=True)
    cd = sum(di for di, ti in ss[:K])
    ct = len(mst)
    m = cd + ct * ct
    for (gdi, gti), (hdi, hti) in zip(reversed(gs), hs):
        cd += hdi - gdi
        ct += 1
        m = max(m, cd + ct * ct)
    print(m)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    t = [int()] * (N)  # type: "List[int]"
    d = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        t[i] = int(next(tokens))
        d[i] = int(next(tokens))
    solve(N, K, t, d)


def __starting_point():
    main()

__starting_point()
