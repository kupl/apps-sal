import math
import sys


def solve(n, q):
    servers = [0] * n
    res = [None] * q
    for j, line in enumerate(sys.stdin):
        t, k, d = list(map(int, line.split()))
        S, m = k, k
        logs = servers[:]
        for i, s in enumerate(servers):
            if s <= t:
                servers[i] = t + d
                S += i
                m -= 1
            if m == 0:
                res[j] = S
                break
        else:
            res[j] = -1
            servers = logs[:]

    return res


n, q = list(map(int, input().split()))
print('\n'.join(map(str, solve(n, q))))
