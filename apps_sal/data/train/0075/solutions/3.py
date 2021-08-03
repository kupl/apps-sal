import math


def sqare_size(n):
    return math.sin((2 * n - 1) / (4 * n) * math.pi) / math.sin(math.pi / (2 * n))


t = int(input())
for _ in range(t):
    print(sqare_size(int(input())))
