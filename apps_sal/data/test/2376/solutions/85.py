def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil

    n, W = map(int, input().split())
    w, v = [], []
    for i in range(n):
        a, b = map(int, input().split())
        if i == 0:
            w.append(a)
        else:
            w.append(a - w[0])
        v.append(b)
    base = w[0]
    w[0] = 0
    w0, w1, w2, w3 = [], [], [], []
    for i in range(n):
        if w[i] == 0:
            w0.append(v[i])
        if w[i] == 1:
            w1.append(v[i])
        if w[i] == 2:
            w2.append(v[i])
        if w[i] == 3:
            w3.append(v[i])
    w0.sort(reverse=1)
    w1.sort(reverse=1)
    w2.sort(reverse=1)
    w3.sort(reverse=1)
    w0 = [0] + w0
    w1 = [0] + w1
    w2 = [0] + w2
    w3 = [0] + w3
    w0 = list(accumulate(w0))
    w1 = list(accumulate(w1))
    w2 = list(accumulate(w2))
    w3 = list(accumulate(w3))

    res = 0
    for i in range(len(w0)):
        for j in range(len(w1)):
            for k in range(len(w2)):
                for l in range(len(w3)):
                    if base * (i + j + k + l) + j + k * 2 + l * 3 <= W:
                        res = max(res, w0[i] + w1[j] + w2[k] + w3[l])
    print(res)


def __starting_point():
    main()


__starting_point()
