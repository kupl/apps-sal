import sys
from heapq import *

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
res = 0


def resolve():
    n, k, q = list(map(int, input().split()))
    A = list(map(int, input().split()))

    res = f_inf
    for i in range(n):
        section = []
        pick = []
        for j in range(n):
            if A[j] < A[i]:
                l = len(section) - k + 1
                for _ in range(l):
                    pick.append(heappop(section))
                section.clear()
            else:
                heappush(section, A[j])
        l = len(section) - k + 1
        for _ in range(l):
            pick.append(heappop(section))

        if len(pick) >= q:
            pick.sort()
            res = min(res, pick[q - 1] - pick[0])
    print(res)


def __starting_point():
    resolve()


__starting_point()
