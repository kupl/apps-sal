import math


def solve():
    (x, y, n) = list(map(int, input().split()))
    rem = n // x
    rem *= x
    rem += y
    if rem > n:
        rem -= x
    print(rem)


t = 1
t = int(input())
for _ in range(0, t):
    solve()
