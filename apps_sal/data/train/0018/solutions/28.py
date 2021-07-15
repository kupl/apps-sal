import os
import sys
if os.path.exists('/mnt/c/Users/Square/square/codeforces'):
    f = iter(open('C.txt').readlines())
    def input():
        return next(f).strip()
    # input = lambda: sys.stdin.readline().strip()  
else:
    input = lambda: sys.stdin.readline().strip()

fprint = lambda *args: print(*args, flush=True)

import math

t = int(input())
for _ in range(t):
    n = int(input())
    print(1.0 / math.tan(math.pi / 2 / n))
