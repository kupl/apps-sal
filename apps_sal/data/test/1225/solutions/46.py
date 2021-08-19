import sys
import copy
import math
import itertools
H = int(input())
cnt = 0
for i in range(int(math.log2(H)) + 1):
    cnt += 2 ** i
print(cnt)
