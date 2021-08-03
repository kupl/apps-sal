from math import *
from sys import *
input = stdin.readline

for _ in range(int(input())):

    n = int(input())
    g = -1

    for i in range(2, int(sqrt(n)) + 1):
        if(n % i == 0):
            g = i
            break

    if(g == -1):
        print(n - 1, 1)
        continue

    a = n // g
    b = (n // g) * (g - 1)

    print(a, b)
