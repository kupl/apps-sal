import sys
import numpy as np
from numba import njit


def input(): return sys.stdin.readline()


N, Q = list(map(int, input().split()))

C = np.array(input().split(), int)

queries = np.empty((Q, 2), int)

for q in range(Q):
    l, r = list(map(int, input().split()))
    queries[q][0] = l
    queries[q][1] = r


orderByR = np.argsort(queries[:, 1])

mostRightColorIndex = np.zeros(N + 1, int)
bitArray = np.zeros(N + 1, int)


@njit
def main(N, Q, C, queries, orderByR, mostRightColorIndex, bitArray):

    def add(itemCount, items, i, value):
        while i <= itemCount:
            items[i] += value
            i += (i & (-i))

    def sumFromStart(items, end):
        summary = 0
        i = end
        while i > 0:
            summary += items[i]
            i -= (i & (-i))
        return summary

    def sum(items, start, end):
        summary = sumFromStart(items, end) - sumFromStart(items, start - 1)
        return summary

    ans = [0] * Q
    qindex = 0

    for n in range(N):

        if Q <= qindex:
            break

        if 0 < mostRightColorIndex[C[n]]:
            add(N, bitArray, mostRightColorIndex[C[n]], -1)

        mostRightColorIndex[C[n]] = n + 1
        add(N, bitArray, n + 1, 1)

        while qindex < Q and n + 1 == queries[orderByR[qindex]][1]:
            tmpIndex = orderByR[qindex]
            start = queries[tmpIndex][0]
            end = queries[tmpIndex][1]
            ans[tmpIndex] = sum(bitArray, start, end)
            qindex += 1

    return ans


for a in main(N, Q, C, queries, orderByR, mostRightColorIndex, bitArray):
    print(a)
