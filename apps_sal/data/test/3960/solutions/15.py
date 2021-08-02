import math


def getMax(a, n):
    MAX = -1 * pow(10, 9)
    memoize = [[0 for x in range(2)] for y in range(n)]
    difference = [0 for x in range(n)]
    for i in range(n):
        if i > 0:
            difference[i] = abs(a[i] - a[i - 1])
    for i in range(1, n):
        memoize[i][0] = max(difference[i], memoize[i - 1][1] + difference[i])
        memoize[i][1] = max(-difference[i], memoize[i - 1][0] - difference[i])
        MAX = max(memoize[i][1], MAX)
        MAX = max(memoize[i][0], MAX)
    return MAX


n = int(input())
a = [int(x) for x in input().split()]
print(getMax(a, n))
