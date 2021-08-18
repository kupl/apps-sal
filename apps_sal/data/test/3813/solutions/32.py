from collections import defaultdict, deque

import numpy as np


def solve(*args: str) -> str:
    n = int(args[0])
    P = list(map(int, args[1].split()))
    X = list(map(int, args[2].split()))

    T = defaultdict(set)
    for i, p in enumerate(P):
        T[p - 1].add(i + 1)

    stack = []
    Q = deque()
    Q.append(0)
    while Q:
        i = Q.popleft()
        stack.append(i)
        for c in T[i]:
            Q.append(c)

    ret = 'POSSIBLE'
    inf = 2**32 - 1
    Y = [0] * n
    for i in stack[::-1]:
        prev = np.full(X[i] + 1, inf, np.int64)
        prev[0] = 0
        x_acc, y_acc = 0, 0
        for c in T[i]:
            cur = np.full(X[i] + 1, inf, np.int64)
            x, y = X[c], Y[c]
            x_acc += x
            y_acc += y
            cur[x:] = np.minimum(cur[x:], y + prev[:-x if 0 < x else len(prev)])
            cur[y:] = np.minimum(cur[y:], x + prev[:-y if 0 < y else len(prev)])
            prev = np.copy(cur)

        y = np.min(prev)
        if y < inf:
            Y[i] = y
        else:
            ret = 'IMPOSSIBLE'
            break

    return ret


def __starting_point():
    print((solve(*(open(0).read().splitlines()))))


__starting_point()
