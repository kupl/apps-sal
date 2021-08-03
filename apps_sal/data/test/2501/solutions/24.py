import sys
from bisect import bisect_right, bisect_left
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    A_i, A_j = [], []
    for i in range(n):
        A_i.append(-A[i] - (i + 1))

    for j in range(n):
        A_j.append(A[j] - (j + 1))

    A_j.sort()

    res = 0
    for a in A_i:
        idx_1 = bisect_left(A_j, a)
        idx_2 = bisect_right(A_j, a)
        res += idx_2 - idx_1
    print(res)


def __starting_point():
    resolve()


__starting_point()
