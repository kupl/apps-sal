from sys import stdin, stdout
from itertools import combinations
from collections import defaultdict, OrderedDict
import math
import heapq


def listIn():
    return list(list(map(int, stdin.readline().strip().split())))


def stringListIn():
    return [x for x in stdin.readline().split()]


def intIn():
    return int(stdin.readline())


def stringIn():
    return stdin.readline().strip()


def perfectSquare(k):
    s = math.sqrt(k)
    if s - int(s) == 0:
        return 1
    else:
        return 0


def check(a, b, op, i):
    (e1, e2) = (a, b)
    if op == '-':
        diff = e2 - e1
    else:
        diff = e2 + e1
    if perfectSquare(diff):
        if diff - arr[i - 1] > 0 or i == 0:
            arr[i] = diff
            arr[i + 1] = e2
            return 1
        else:
            return 0
    else:
        return 0


def __starting_point():
    n = intIn()
    even = listIn()
    arr = [0] * n
    j = 0
    for i in range(n):
        if i % 2 != 0:
            arr[i] = even[j]
            j += 1
    k = 0
    l = 0
    s = 0
    zcnt = 0
    b_end = 10 ** 13
    flag = False
    for i in range(0, n, 2):
        found = False
        while not found:
            k += 1
            if k * k - s > b_end:
                print('No')
                return
            forward_sum = k * k + arr[i + 1]
            while forward_sum > l * l:
                l += 1
            if forward_sum == l * l:
                found = True
                arr[i] = k * k - s
                s = forward_sum
                k = l
    print('Yes')
    print(*arr)


__starting_point()
