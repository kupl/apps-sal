#import resource
import math
from collections import deque
import sys

#resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10 ** 7)

n = int(input())

a = [int(x) for x in input().strip().split()]

ok = True
for x in a:
    if ((x & 1) == 0):
        ok = ok and ((x % 3) == 0 or (x % 5) == 0)
if ok:
    print("APPROVED")
else:
    print("DENIED")
