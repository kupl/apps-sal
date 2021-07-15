from math import *
for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    if n <= 2:
        print(1)
    else:
        print(1 + (n - 2 + x - 1) // x)
