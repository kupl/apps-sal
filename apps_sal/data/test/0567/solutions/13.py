import sys
import math
f = sys.stdin
n = f.readline()
s = list(map(int, f.readline().split()))
print(max((min(x - 1, 1000000 - x) for x in s)))
