import numpy as np
n = int(input())
(x, y) = np.array([list(map(int, input().split())) for _ in range(n)]).T


def isin90deg(v1, v2):
    if np.dot(v1, v2) >= 0:
        return 1
    else:
        return 0


def is90deg(v1, v2):
    if np.dot(v1, v2) == 0:
        return 1
    else:
        return 0


ans = []
for i in range(n):
    (tv, nv1) = (np.array([x[i], y[i]]), np.array([y[i], -x[i]]))
    nv2 = -nv1
    for nv in [nv1, nv2]:
        (sum, posi, nega) = (np.array([0, 0]), np.array([0, 0]), np.array([0, 0]))
        for j in range(n):
            v = np.array([x[j], y[j]])
            if isin90deg(v, nv):
                sum += v
            if is90deg(v, nv) and isin90deg(v, tv):
                posi += v
            if is90deg(v, nv) and (not isin90deg(v, tv)):
                nega += v
        ans.append(np.linalg.norm(sum, ord=2))
        ans.append(np.linalg.norm(sum - posi, ord=2))
        ans.append(np.linalg.norm(sum - nega, ord=2))
print(max(ans))
