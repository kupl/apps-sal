import sys
import os


def extract(a):
    d = dict()
    r = []
    for e in a:
        if not e in d:
            r.append(1)
            d[e] = d
        else:
            r.append(0)

    return r


def sonyaAndRobots(n, a):
    t1 = extract(a)
    t2 = list(reversed(extract(reversed(a))))

    for i in range(n - 1):
        t1[i + 1] += t1[i]

    result = 0
    for i in range(n - 1):
        result += t1[i] * t2[i + 1]

    return result


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    print(sonyaAndRobots(n, a))


def __starting_point():
    main()


__starting_point()
