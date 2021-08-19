import math
import bisect
from collections import defaultdict as df
from collections import deque
from sys import stdin, stdout
t = int(input())
for i in range(t):
    (n, x, a, b) = list(map(int, input().split()))
    p = [a, b]
    p.sort()
    (a, b) = p
    room = a - 1 + n - b
    mini = min(room, x)
    ans = b - a + mini
    print(ans)
