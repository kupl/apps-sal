import math
import sys
sys.setrecursionlimit(10 ** 6)
(a, b) = list(map(int, input().split()))
print(math.ceil((a + b) / 2))
