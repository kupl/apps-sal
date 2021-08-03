import sys
import math


def solution(n, m, a, b):
    a += [a[0]]
    b += [b[0]]
    mass = [0] * len(a)
    mass[len(a) - 1] = m
    for i in range(len(a) - 1, 0, -1):
        tmp = mass[i]
        if b[i] - 1 <= 0:
            return -1
        extra_fuel = tmp / (b[i] - 1)
        tmp += extra_fuel
        if a[i - 1] - 1 <= 0:
            return -1
        extra_fuel = tmp / (a[i - 1] - 1)
        tmp += extra_fuel
        mass[i - 1] = tmp

    return mass[0] - m


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

a = [int(x) for x in sys.stdin.readline().rstrip().split()]
b = [int(x) for x in sys.stdin.readline().rstrip().split()]

res = solution(n, m, a, b)

sys.stdout.write(str(res))
