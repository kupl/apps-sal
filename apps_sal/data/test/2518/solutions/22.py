import sys
from heapq import heapify, heappop, heappush
from collections import defaultdict


def main():

    def finput():
        return sys.stdin.readline().strip()
    (n, a, b) = list(map(int, finput().split()))
    h = [int(finput()) for _ in range(n)]

    def gs(a, b):
        return a // b + (a % b > 0)

    def enough(t):
        s = sum([gs(max(x - t * b, 0), a - b) for x in h])
        if s <= t:
            return True
        else:
            return False

    def biser(t, l):
        if l == 0:
            return t
        t = t + l // 2
        if enough(t):
            return biser(t - l // 2, l // 2)
        else:
            return biser(t + 1, l - l // 2)
    l = max(h) // b + 1
    t = biser(0, l)
    print(t)


def __starting_point():
    main()


__starting_point()
