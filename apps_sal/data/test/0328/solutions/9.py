import os
import sys
n = int(sys.stdin.readline())
res = 0
for _ in range(n):
    (x, y) = [int(s) for s in sys.stdin.readline().split()]
    if x + y > res:
        res = x + y
sys.stdout.write('{0}'.format(res))
