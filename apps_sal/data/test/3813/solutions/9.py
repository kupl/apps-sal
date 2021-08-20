import numpy as np


def solve(*args: str) -> str:
    n = int(args[0])
    P = list(map(int, args[1].split()))
    X = list(map(int, args[2].split()))
    T = [[] for _ in range(n)]
    for (i, p) in enumerate(P):
        T[p - 1].append(i + 1)
    seq = []
    stack = [0]
    while stack:
        i = stack.pop()
        seq.append(i)
        for c in T[i]:
            stack.append(c)
    ret = 'POSSIBLE'
    inf = 2 ** 32 - 1
    Y = [0] * n
    for i in seq[::-1]:
        prev = np.full(X[i] + 1, inf, np.int64)
        prev[0] = 0
        for c in T[i]:
            cur = np.full(X[i] + 1, inf, np.int64)
            (x, y) = (X[c], Y[c])
            cur = np.minimum(np.concatenate((cur[:x], y + prev[:-x if 0 < x else len(prev)])), np.concatenate((cur[:y], x + prev[:-y if 0 < y else len(prev)])))
            prev = np.copy(cur)
        y = np.min(prev)
        if y < inf:
            Y[i] = y
        else:
            ret = 'IMPOSSIBLE'
            break
    return ret


def __starting_point():
    print(solve(*open(0).read().splitlines()))


__starting_point()
