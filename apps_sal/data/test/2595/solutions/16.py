from sys import stdin, stdout
from math import ceil


def solve(a, b):
    x = max(a, b)
    y = min(a, b)
    c = 0
    while x != y:
        if x % 2:
            print(-1)
            return True
        c += 1
        x //= 2
    print(ceil(c / 3))
    return True


for _ in range(int(input())):
    n, m = map(int, stdin.readline().split())
    solve(n, m)
