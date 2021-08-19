import sys
from math import gcd
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    mx = max(a)
    table = [0] * (mx + 1)
    for x in a:
        table[x] += 1
    res = [mx]
    table[mx] -= 1
    g = mx
    for _ in range(N - 1):
        y = 0
        for x in range(1, mx + 1):
            if table[x] == 0:
                continue
            if y == 0 or gcd(g, x) > gcd(g, y):
                y = x
        table[y] -= 1
        res.append(y)
        g = gcd(g, y)
    print(*res)
