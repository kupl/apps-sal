import sys
import math
from itertools import permutations
input = sys.stdin.readline

n = int(input())

minn = n // 2 + 1
print(minn)
for i in range(minn):
    print(1, i + 1)
left = n - minn
for i in range(left):
    print(i + 2, minn)
