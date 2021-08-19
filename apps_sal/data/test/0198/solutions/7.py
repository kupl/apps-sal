import itertools
import math
n = int(input())
if n % 2:
    print(0)
else:
    m = n // 2
    print((m - 1) // 2)
