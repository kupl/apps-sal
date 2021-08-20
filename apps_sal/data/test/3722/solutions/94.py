import sys
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate
sys.setrecursionlimit(10 ** 6)
INF = 10 ** 12
m = 10 ** 9 + 7


def main():
    N = int(input())
    caa = input()
    cab = input()
    cba = input()
    cbb = input()
    if N < 4:
        print(1)
        return
    if cab == 'B':
        if cbb == 'B':
            print(1)
        elif cba == 'A':
            print(pow(2, N - 3, m))
        else:
            f = [1, 2]
            for i in range(N - 4):
                f.append((f[-1] + f[-2]) % m)
            print(f[-1])
    elif caa == 'A':
        print(1)
    elif cba == 'B':
        print(pow(2, N - 3, m))
    else:
        f = [1, 2]
        for i in range(N - 4):
            f.append((f[-1] + f[-2]) % m)
        print(f[-1])


def __starting_point():
    main()


__starting_point()
