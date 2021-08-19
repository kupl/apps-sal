import sys


def input():
    return sys.stdin.readline().strip()


for i in range(int(input())):
    (a, b, x, y) = map(int, input().split())
    print(max(a * y, b * x, a * (b - y - 1), b * (a - x - 1)))
