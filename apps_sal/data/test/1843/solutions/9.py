import math


def cal(val):
    k = int(math.log2(val))
    return (1 + val) * val // 2 - 2 * (2 ** (k + 1) - 1)


N = int(input())
for i in range(N):
    print(cal(int(input())))
