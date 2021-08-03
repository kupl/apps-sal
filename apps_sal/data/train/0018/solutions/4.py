import math


def sqare_size(n):
    return 1 / math.tan(math.pi / (2 * n))


t = int(input())
for _ in range(t):
    print(sqare_size(int(input())))
