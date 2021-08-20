import sys
from heapq import heapify, heappop, heappush
from collections import defaultdict


def finput():
    return sys.stdin.readline().strip()


def main():
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
    l = max(h) // b + 1
    t = 0
    while l > 0:
        t = t + l // 2
        if enough(t):
            t = t - l // 2
            l = l // 2
        else:
            t += 1
            l = l - l // 2
    print(t)


def __starting_point():
    main()


__starting_point()
