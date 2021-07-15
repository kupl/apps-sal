import os
from io import BytesIO

# input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
for i in range(int(input())):
    a, b, c, r = list(map(int, input().split()))
    a, b = min(a, b), max(a, b)
    left = max(c - r, a)
    right = min(c + r, b)
    if right >= a and left <= right:
        print(b - a - (right - left))
    else:
        print(b - a)

