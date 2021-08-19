import sys
import math
from collections import defaultdict as dd
mod = 1000000007
T = 1
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(input())
    l = list(map(int, input().split()))
    if sum(l) == n:
        if n & 1:
            print('First')
        else:
            print('Second')
        continue
    x = 0
    for i in range(n):
        if l[i] != 1:
            x = i
            break
    if True:
        if x & 1:
            print('Second')
        else:
            print('First')
