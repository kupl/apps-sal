# import math
# import sys

n, v = [int(x) for x in input().strip().split(" ")]
if v >= (n - 1):
    print(n - 1)
else:
    print(n - 1 + ((n - 1 - v) * (n - v) // 2))
