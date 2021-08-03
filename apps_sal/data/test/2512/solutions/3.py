import sys
import numpy as np
from collections import defaultdict
from numba import njit
def input(): return sys.stdin.readline().rstrip()


@njit
def koushin(dp, item):
    dptmp1 = np.copy(dp)
    dptmp2 = np.copy(dp)
    dptmp3 = np.copy(dp)
    for i in range(len(item)):
        dptmp3[item[i][0]:] = np.fmax(dptmp3[item[i][0]:], dptmp2[item[i][0]] + item[i][1])
        dptmp2[item[i][0]:] = np.fmax(dptmp2[item[i][0]:], dptmp1[item[i][0]] + item[i][1])
        dptmp1[item[i][0]:] = np.fmax(dptmp1[item[i][0]:], dp[item[i][0]] + item[i][1])
    return dptmp3


def main():
    R, C, K = map(int, input().split())
    items = defaultdict(list)
    for _ in range(K):
        r, c, v = map(int, input().split())
        items[r - 1].append([c - 1, v])
    dp = np.zeros(C, dtype=int)
    for RR in range(R):
        if items[RR] == []:
            continue
        items[RR].sort(key=lambda x: x[0])
        dp = koushin(dp, np.array(items[RR], dtype=int))
    print(dp[-1])


def __starting_point():
    main()


__starting_point()
