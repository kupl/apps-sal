from math import *


def sum(n):
    return (n * (n + 1)) // 2


m, b = [int(x) for x in input().strip().split()]
ans = 0
x = 0
y = 0
while True:
    if b < y:
        break
    x = m * (b - y)
    rans = sum(x) * (y + 1) + sum(y) * (x + 1)
    ans = max(ans, rans)
    y += 1
print(ans)

