import sys
from collections import defaultdict
from bisect import bisect_right

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    n = len(S)
    T = input()

    pos = defaultdict(list)
    for i in range(n):
        pos[S[i]].append(i + 1)

    res = 0
    now = 0
    for t in T:
        if pos.get(t, -1) == -1:
            print((-1))
            return
        idx = bisect_right(pos[t], now)
        if len(pos[t]) == idx:
            res += n - now + pos[t][0]
            now = pos[t][0]
        else:
            res += pos[t][idx] - now
            now = pos[t][idx]
    print(res)


def __starting_point():
    resolve()


__starting_point()
