import sys
from heapq import *

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k, q = list(map(int, input().split()))
    A = list(map(int, input().split()))

    res = f_inf
    for a in A:
        section = []
        tmp = []
        for b in A:
            if b < a:
                if len(tmp) >= k:
                    section.append(tmp)
                tmp = []
            else:
                heappush(tmp, b)
        if len(tmp) >= k:
            section.append(tmp)

        kouho = []
        for sec in section:
            while len(sec) >= k:
                kouho.append(heappop(sec))

        if len(kouho) >= q:
            kouho.sort()
            x = kouho[q - 1]
            y = kouho[0]
            res = min(res, x - y)

    print(res)


def __starting_point():
    resolve()


__starting_point()
