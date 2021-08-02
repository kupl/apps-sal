import sys
import math
from math import factorial as f
from collections import defaultdict as dd
mod = 1000000007
T = 1
T = int(sys.stdin.readline())
for _ in range(T):
    s = input()
    ans = ''
    for i in range(0, len(s), 2):
        ans += s[i]
    print(ans + s[-1])
