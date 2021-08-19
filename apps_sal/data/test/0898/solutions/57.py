import sys
import math
from collections import deque
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def NI():
    return int(input())


def NMI():
    return map(int, input().split())


def NLI():
    return list(NMI())


def SI():
    return input()


def make_grid(h, w, num):
    return [[int(num)] * w for _ in range(h)]


def main():
    (N, M) = NMI()
    yak = set()
    i = 1
    while i * i <= M:
        if M % i == 0:
            yak.add(i)
            yak.add(M // i)
        i += 1
    yak = sorted(list(yak), reverse=True)
    for y in yak:
        if y * N <= M:
            print(y)
            return


def __starting_point():
    main()


__starting_point()
