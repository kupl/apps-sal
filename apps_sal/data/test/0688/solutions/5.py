import sys


def solve():
    first = list(input())
    second = list(input())
    first = map(int, first)
    second = map(int, second)
    count = [0] * 10
    for i in first:
        count[m(i)] += 1
    total = [0] * 10
    for i in second:
        total[m(i)] += 1
    res = 0
    while True:
        for i in range(10):
            total[i] -= count[i]
        for i in range(10):
            if total[i] < 0:
                return res
        res += 1
    return res


def m(c):
    if c == 9:
        return 6
    if c == 5:
        return 2
    return c


if sys.hexversion == 50594544:
    sys.stdin = open('test.txt')
print(solve())
