import sys
import math
from collections import deque
sys.setrecursionlimit(10**9)


def input():
    return sys.stdin.readline()[:-1]


def mi():
    return map(int, input().split())


def ii():
    return int(input())


def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def main():
    N, K = mi()
    S = input()

    m = S.count('RL') + S.count('LR')
    x = (N - 1) - m

    print(min(x + 2 * K, N - 1))


def __starting_point():
    main()


__starting_point()
