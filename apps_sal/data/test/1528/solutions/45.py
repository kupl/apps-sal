from collections import defaultdict
3
(N, X) = (int(x) for x in input().split())
memo = {}


def size_lv(lv):
    if lv == 0:
        return 1
    if lv not in memo:
        memo[lv] = size_lv(lv - 1) * 2 + 3
    return memo[lv]


memo2 = {}


def num_pty(lv, X):
    if (lv, X) in memo2:
        return memo2[lv, X]
    if X == 0:
        return 0
    if lv == 0:
        memo2[lv, X] = 1
        return memo2[lv, X]
    prevSize = size_lv(lv - 1)
    if X <= prevSize + 1:
        memo2[lv, X] = num_pty(lv - 1, X - 1)
        return memo2[lv, X]
    if X == prevSize + 2:
        memo2[lv, X] = num_pty(lv - 1, prevSize) + 1
        return memo2[lv, X]
    memo2[lv, X] = num_pty(lv - 1, prevSize) + 1 + num_pty(lv - 1, min(X - prevSize - 2, prevSize))
    return memo2[lv, X]


print(num_pty(N, X))
