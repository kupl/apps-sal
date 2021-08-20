import sys
from math import ceil
input_file = sys.stdin
[n, s] = list((int(x) for x in input_file.readline().split()))
print(ceil(s / n))
