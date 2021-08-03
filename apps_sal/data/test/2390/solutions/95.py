import numpy as np
import itertools
N, C, *XV = [int(_) for _ in open(0).read().split()]
XV = [0, 0] + XV
XV = np.array(XV).reshape((N + 1, 2))
YV = np.zeros((N + 1, 2), dtype=np.int64)
YV[1:] = XV[:0:-1]
YV[1:, 0] *= -1
YV[1:, 0] += C


def calc(XV, YV):
    cumxvv = np.cumsum(XV[:, 1])
    cumxvv -= 2 * XV[:, 0]
    cumyvv = np.cumsum(YV[:, 1])
    cumyvv -= YV[:, 0]
    cummaxyvv = list(itertools.accumulate(cumyvv, func=lambda a, b: a if a > b else b))
    ans = -float('inf')
    for i in range(N + 1):
        ans = max(ans, cumxvv[i] + cummaxyvv[N - i])
    return ans


print((max(calc(XV, YV), calc(YV, XV))))
