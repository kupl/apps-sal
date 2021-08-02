import math
import time
from collections import defaultdict, deque
from sys import stdin, stdout
from bisect import bisect_left, bisect_right
t = 1
t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for i in range(1, (n + 1) // 2):
        ans += i * 8 * i
    print(ans)
