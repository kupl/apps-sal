import sys
import math

n = int(sys.stdin.readline())
an = [int(x) for x in (sys.stdin.readline()).split()]

vsum = sum(an)

res = 0
for i in range(1, 6):
    if((i + vsum) % (n + 1) != 1):
        res += 1

print(res)
