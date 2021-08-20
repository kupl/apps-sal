import math
import os
import sys
if os.path.exists('/mnt/c/Users/Square/square/codeforces'):
    f = iter(open('C.txt').readlines())

    def input():
        return next(f).strip()
else:

    def input():
        return sys.stdin.readline().strip()
fprint = lambda *args: print(*args, flush=True)
t = int(input())
for _ in range(t):
    n = int(input())
    print(1.0 / math.tan(math.pi / 2 / n))
