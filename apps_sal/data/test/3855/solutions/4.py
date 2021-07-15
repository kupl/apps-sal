from sys import stdin, stdout
from collections import deque
from math import log10


n = int(stdin.readline())
ans = 0

for i in range(0, 31):
    if (1 << i) <= n:
        ans += 1

stdout.write(str(ans))
