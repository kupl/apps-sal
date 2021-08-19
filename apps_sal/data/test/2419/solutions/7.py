from random import *
n = int(input())
for _ in range(n):
    (a, b) = map(int, input().split())
    c = abs(a - b)
    s = 0
    i = 1
    while s < c or (s + c) % 2 != 0:
        s += i
        i += 1
    print(i - 1)
