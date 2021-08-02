# template
import sys
sys.setrecursionlimit(10**9)

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

read_int = lambda: int(readline())
read_ints = lambda: map(int, readline().split())
read_ints_list = lambda: list(map(int, readline().split()))
read_ints_grid = lambda h: list(list(map(int, readline().split())) for _ in range(h))
read_strs_list = lambda: list(map(str, readline().rstrip().split()))
read_strs_grid = lambda h: list(list(map(str, readline().rstrip().split())) for _ in range(h))


def read_allints_grid(w):
    grid = map(int, read().split())
    grid = list(map(list, zip(*(grid for _ in range(w)))))
    return grid


def read_allstrs_grid(w):
    grid = map(str, read().split())
    grid = list(map(list, zip(*(grid for _ in range(w)))))
    return grid

# import
# from copy import deepcopy
# from decimal import Decimal
# from math import ceil,floor
# from collections import deque,Counter
# from heapq import heapify,heappop,heappush
# from itertools import accumulate,product,permutations,combinations,combinations_with_replacement
# from bisect import bisect_left,bisect_right

# solution


def sol():
    return None


def GCD(a: int, b: int) -> int:
    '''
    ユークリッドの互除法による最大公約数/O(log min(a,b))
    '''
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


def GCD_multi(vec: list) -> int:
    '''
    数列の要素の最大公約数を求める/O(N log(a'))
    '''
    l = vec[0]
    for i in range(len(vec) - 1):
        l = GCD(l, vec[i + 1])
    return l


def main():
    # input data
    n = read_int()
    A = read_ints_list()

    # solve
    print(GCD_multi(A))


def __starting_point():
    main()


__starting_point()
