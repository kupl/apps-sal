import sys
import math
import queue
import bisect
MOD = 10 ** 9 + 7
sys.setrecursionlimit(1000000)
for _ in range(int(input())):
    (k, n, a, b) = map(int, input().split())
    x = (k - n * b) // (a - b)
    if k <= n * b:
        print(-1)
    elif (k - n * b) % (a - b) == 0:
        print(min(x - 1, n))
    else:
        print(min(x, n))
