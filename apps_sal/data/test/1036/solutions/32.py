import sys
sys.setrecursionlimit(5000)
n, k = list(map(int, input().split()))
s = input()
win = {"R": "S", "P": "R", "S": "P"}
memo = [[-1] * (k + 1) for _ in range(n + 1)]


def rec(idx, k):
    if k == 0:
        return s[idx]
    if memo[idx][k] != -1:
        return memo[idx][k]

    idxr = (idx + pow(2, k - 1)) % n
    lte = rec(idx, k - 1)
    rte = rec(idxr, k - 1)
    if lte == rte:
        winte = lte
    else:
        if win[lte] == rte:
            winte = lte
        else:
            winte = rte
    memo[idx][k] = winte
    return winte


w = rec(0, k)
print(w)
