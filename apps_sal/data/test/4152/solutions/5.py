import sys
import os


def powerOfTwo(arr):
    p2 = set()
    for i in range(32):
        p2.add(2**i)

    x = set()
    pending = dict()
    for e in arr:
        if e in pending:
            if e in p2:
                del(pending[e])
            else:
                pending[e] += 1
            continue
        if e in x:
            continue

        found = False
        t = 1
        for i in range(32):
            if t - e in x:
                found = True
            if t - e in pending:
                del(pending[t - e])
            t *= 2

        if not found:
            if e in pending:
                pending[e] += 1
            else:
                pending[e] = 1

        x.add(e)

    result = 0
    for _, v in pending.items():
        result += v

    return result


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(powerOfTwo(arr))


def __starting_point():
    main()


__starting_point()
