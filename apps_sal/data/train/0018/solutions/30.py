from math import *
for _ in range(int(input())):
    n = 2 * int(input())
    a = pi - pi * (n - 2) / n
    ans = 0
    for i in range(1, n // 4):
        ans += cos(i * a)
    print(2 * ans + 1)
