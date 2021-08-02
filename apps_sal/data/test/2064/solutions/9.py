from math import *
n = int(input())
if n % 2 != 0:
    n -= 3;
    print(7, end="")
i = 0
while i < n:
    i += 2
    print(1, end="")
