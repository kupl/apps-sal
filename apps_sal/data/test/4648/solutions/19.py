
import math


def solve():
    n = int(input())
    p2, p3 = 0, 0
    while n % 2 == 0:
        p2 += 1
        n //= 2
    while n % 3 == 0:
        p3 += 1
        n //= 3
    if p3 < p2:
        print(-1)
    else:
        if n != 1:
            print(-1)
        else:
            print((p3 - p2) + p3)


t = 1
t = int(input())
for _ in range(0, t):
    solve()
