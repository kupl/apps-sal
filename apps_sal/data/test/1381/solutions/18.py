import sys
import math
(k, n, s, p) = list(map(int, sys.stdin.readline().strip().split(' ')))
print(math.ceil(k * math.ceil(n / s) / p))
