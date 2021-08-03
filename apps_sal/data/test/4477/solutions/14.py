import math
from bisect import bisect_right
from collections import defaultdict as dc
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    x = n % 10
    c = 10 * (x - 1)
    s = str(n)
    for i in range(len(s)):
        c += i + 1
    print(c)
