import math
import sys


a, b = map(int, input().split())
count = 0

for i in range(int(math.log2(a)) - 1, int(math.log2(b)) + 1):
    base = 2 ** (i + 1) - 1
    for j in range(i):
        if a <= (base - 2 ** j) <= b:
            count += 1

print(count)
