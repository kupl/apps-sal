
from collections import defaultdict
import sys
sys.setrecursionlimit(1 << 25)
read = sys.stdin.readline


def read_ints():
    return list(map(int, read().split()))


def read_col(H, n_cols):
    '''
    H is number of rows
    n_cols is number of cols
    A列、B列が与えられるようなとき
    '''
    ret = [[] for _ in range(n_cols)]
    for _ in range(H):
        tmp = list(map(int, read().split()))
        for col in range(n_cols):
            ret[col].append(tmp[col])
    return ret


N, W = read_ints()
w, v = read_col(N, 2)

dp = defaultdict(lambda: -1)


def f(i, j):
    if dp[i, j] != -1:
        return dp[i, j]
    if i == -1:
        return 0
    if j - w[i] < 0:
        return f(i - 1, j)

    ret = max(f(i - 1, j - w[i]) + v[i], f(i - 1, j))
    dp[i, j] = ret
    return ret


print((f(N - 1, W)))
