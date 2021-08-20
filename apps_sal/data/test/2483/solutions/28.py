from collections import defaultdict
import numpy as np
import sys
sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    (N, C) = list(map(int, input().split()))
    MAX = 10 ** 5 + 2
    vals = [0] * MAX
    D = defaultdict(list)
    for _ in range(N):
        (s, t, c) = list(map(int, input().split()))
        D[c].append((s, t))
    for (k, v) in list(D.items()):
        prev = -1
        v.sort(key=lambda x: x[0])
        for (s, t) in v:
            if prev == s:
                vals[prev + 1] += 1
                vals[t + 1] -= 1
            else:
                vals[s] += 1
                vals[t + 1] -= 1
            prev = t
    cumsum = np.cumsum(vals)
    ans = max(cumsum)
    print(ans)


def __starting_point():
    main()


__starting_point()
