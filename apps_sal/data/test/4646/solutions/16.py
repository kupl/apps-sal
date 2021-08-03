import sys
import math
from math import factorial as f
from collections import defaultdict as dd
mod = 1000000007
T = 1
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(input())
    l = list(map(int, input().split()))
    c1, c2 = 0, 0
    for i in range(n):
        if(l[i] & 1):
            if i & 1 == 0:
                c1 += 1
        else:
            if(i & 1):
                c2 += 1
    if c1 != c2:
        print(-1)
    else:
        print(c1)
