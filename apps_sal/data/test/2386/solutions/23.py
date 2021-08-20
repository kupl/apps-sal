import sys
from statistics import median
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - (i + 1) for i in range(n)]
    M = int(median(A))
    res = 0
    for a in A:
        res += abs(a - M)
    print(res)


def __starting_point():
    resolve()


__starting_point()
