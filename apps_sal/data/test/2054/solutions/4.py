from math import *
a = int(input())
for _ in range(a):
    (b, c) = map(int, input().split())
    if b >= 2 * c:
        print(c)
    elif c >= 2 * b:
        print(b)
    else:
        print(floor((b + c) / 3))
