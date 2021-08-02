import sys
import math
from functools import reduce

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
# MOD = 10 ** 9 + 7
MOD = 998244353


def input():
    return sys.stdin.readline().strip()


def gcd(nums):
    return reduce(math.gcd, nums)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = gcd(A)
    print(ans)


def __starting_point():
    main()


__starting_point()
