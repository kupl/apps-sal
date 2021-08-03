import functools


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        arr = []

        for i in range(lo, hi + 1):
            arr.append([i, getPower(i)])

        arr.sort(key=functools.cmp_to_key(compareByK))

        return arr[k - 1][0]


def getPower(n):
    steps = 0
    while n != 1:
        steps += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1

    return steps


def compareByK(x, y):
    powerX = x[1]
    powerY = y[1]

    if powerX < powerY:
        return -1
    elif powerX > powerY:
        return 1
    else:
        if x[0] < y[0]:
            return -1
        elif x[0] > y[0]:
            return 1
        else:
            return 0
