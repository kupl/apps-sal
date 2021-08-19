#!/usr/bin/env python3

from collections import defaultdict


def main():
    n, k = list(map(int, input().split()))
    td = []
    for i in range(n):
        ti, di = list(map(int, input().split()))
        td.append((ti, di))
    td = list(reversed(sorted(td)))
    tdd = defaultdict(list)
    for t, d in td:
        tdd[t].append(d)

    a = []
    b = []
    for _, v in list(tdd.items()):
        a.append(v[0])
        b += v[1:]

    a = list(reversed(sorted(a)))
    b = list(reversed(sorted(b)))
    for i in range(1, len(a)):
        a[i] += a[i - 1]
    for i in range(len(a)):
        a[i] += (i + 1) ** 2
    for i in range(1, len(b)):
        b[i] += b[i - 1]

    a = [0] + a
    b = [0] + b

    res = 0
    for i in range(1, k + 1):
        if i >= len(a) or (k - i) >= len(b):
            continue
        ts = a[i] + b[k - i]
        res = max(res, ts)

    print(res)


def __starting_point():
    main()


__starting_point()
