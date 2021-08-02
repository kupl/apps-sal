import math


def ten(p):
    if p == 0:
        return 0
    else:
        return ten(p // 10) + 1


N = int(input())
x = int(math.sqrt(N))
while N % x != 0:
    x -= 1
y = int(N / x)

print((ten(y)))
