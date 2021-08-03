import math
from collections import deque
import sys
from sys import stdin, stderr, stdout


n, k = list(map(int, stdin.readline().strip().split()))
a = n // k
if a % 2 == 1:
    print('YES')
else:
    print('NO')
