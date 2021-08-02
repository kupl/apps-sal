import sys
import math
lines = sys.stdin.read().splitlines()
lincnt = -1


def input():
    nonlocal lincnt
    lincnt += 1
    return lines[lincnt]


def solve():
    x = int(input())
    for n in range(max(1, int(math.sqrt(x) - 5)), int(10**4.7)):
        if n ** 2 <= x:
            continue
        m = math.sqrt(n ** 2 / (n ** 2 - x))
        for k in range(int(m) - 3, int(m) + 3):
            if k < 1:
                continue
            if n ** 2 - (n // k) ** 2 == x:
                print(n, k)
                return
    print(-1)


for _ in range(int(input())):
    solve()
