import numpy as np


def finalFunc(n, s, A):
    var = np.array([0 for i in range(min(3001, s + 1))])
    var[0] = 1
    for i in A:
        tmp = var[:-i].copy()
        var *= 2
        var[i:] += tmp
        var %= 998244353
    return var[s]


n, s = map(int, input().split())
A = list(map(int, input().split()))
print(finalFunc(n, s, A))
