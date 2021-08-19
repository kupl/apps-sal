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


def make_cumulative(A):
    C = [0] * (len(A) + 1)
    for (i, a) in enumerate(A):
        i += 1
        C[i] = C[i - 1] + a
    return C


def main():
    (N, M) = NMI()
    cakes = [[] for _ in range(8)]
    for i in range(N):
        (x, y, z) = NMI()
        cakes[0].append(sum([x, y, z]))
        cakes[1].append(sum([x, y, -z]))
        cakes[2].append(sum([x, -y, z]))
        cakes[3].append(sum([x, -y, -z]))
        cakes[4].append(sum([-x, y, z]))
        cakes[5].append(sum([-x, y, -z]))
        cakes[6].append(sum([-x, -y, z]))
        cakes[7].append(sum([-x, -y, -z]))
    for i in range(8):
        cakes[i] = sorted(cakes[i], reverse=True)
        cakes[i] = sum(cakes[i][:M])
    print(max(cakes))


def __starting_point():
    main()


__starting_point()
