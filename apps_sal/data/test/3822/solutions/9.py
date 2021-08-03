from sys import stdin, stdout
import math


def solution():
    n, l, v1, v2, k = map(int, stdin.readline().rstrip().split())
    grs = math.ceil(float(n) / k)
    c = grs / (v2 - v1) + (grs - 1) / (v1 + v2)
    stdout.write("{}".format(l / (v1 + 1 / c)))


def __starting_point():
    solution()


__starting_point()
