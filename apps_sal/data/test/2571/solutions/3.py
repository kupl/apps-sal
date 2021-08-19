from math import *
import os
import sys
from io import BytesIO

#input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
#sys.stdin = open("input.txt", "r")
#sys.stdout = open("output.txt", "w")

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 == 0:
        for i in range(n // 2):
            print(-a[2 * i + 1], a[2 * i], end=' ')
        print()
    else:
        pass
