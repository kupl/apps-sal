from bisect import bisect_left, bisect_right
from itertools import product, permutations, combinations
from operator import itemgetter
from collections import defaultdict, Counter, deque
import sys
sys.setrecursionlimit(1 << 25)
read = sys.stdin.readline
ra = range
enu = enumerate


def read_ints():
    return list(map(int, read().split()))


def read_a_int():
    return int(read())


def read_tuple(H):
    """
    H is number of rows
    """
    ret = []
    for _ in range(H):
        ret.append(tuple(map(int, read().split())))
    return ret


def read_col(H):
    """
    H is number of rows
    A列、B列が与えられるようなとき
    ex1)A,B=read_col(H)    ex2) A,=read_col(H) #一列の場合
    """
    ret = []
    for _ in range(H):
        ret.append(list(map(int, read().split())))
    return tuple(map(list, zip(*ret)))


def read_matrix(H):
    """
    H is number of rows
    """
    ret = []
    for _ in range(H):
        ret.append(list(map(int, read().split())))
    return ret


MOD = 10 ** 9 + 7
INF = 2 ** 31
(A, B) = read_ints()
A -= 1
B -= 1
print(100, 100)
for _ in range(25):
    for _ in range(50):
        if A > 0:
            print('#.', end='')
            A -= 1
        else:
            print('##', end='')
    print()
    print('#' * 100)
for _ in range(25):
    print('.' * 100)
    for _ in range(50):
        if B > 0:
            print('#.', end='')
            B -= 1
        else:
            print('..', end='')
    print()
