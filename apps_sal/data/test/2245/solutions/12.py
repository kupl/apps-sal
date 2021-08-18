import sys
import math

t = int(input())

for i in range(t):
    n, k = map(int, input().split())

    if k % 3 != 0:
        if n % 3 == 0:
            print("Bob")
        else:
            print("Alice")
    else:
        n += 1
        n = n % (k + 1)
        if n % 3 == 1:
            print("Bob")
        else:
            print("Alice")
