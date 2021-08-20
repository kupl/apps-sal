from math import *
for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print(1 / tan(radians(90 / n)))
