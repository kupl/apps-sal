import sys
from heapq import heapify, heappop, heappush
from collections import defaultdict
import numpy as np


def main():
    finput = lambda: sys.stdin.readline().strip()
    n, a, b = list(map(int, finput().split()))
    h = [int(finput()) for _ in range(n)]
    gs = lambda a, b: a // b + (a % b > 0)

    def enough(t):
        s = np.sum([gs(max(x - t * b, 0), a - b) for x in h])
        if s <= t:
            return True
        else:
            return False
    # def biser(t,l):
    #    if l==0:
    #        return t
    #    t=t+l//2
    #    if enough(t):
    #        return biser(t-l//2,l//2)
    #    else:
    #        return biser(t+1,l-l//2)
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
