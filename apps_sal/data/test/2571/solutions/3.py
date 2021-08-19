from math import *
import os
import sys
from io import BytesIO
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 == 0:
        for i in range(n // 2):
            print(-a[2 * i + 1], a[2 * i], end=' ')
        print()
    else:
        pass
