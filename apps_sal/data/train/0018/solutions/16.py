import math

import sys
input = sys.stdin.readline

Q = int(input())
Query = [int(input()) for _ in range(Q)]

for N in Query:
    if N%2 == 0:
        print(1/math.tan(math.pi/(N*2)))
