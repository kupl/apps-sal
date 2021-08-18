import math
import os
import sys
if os.path.exists('/mnt/c/Users/Square/square/codeforces'):
    f = iter(open('D.txt').readlines())

    def input():
        return next(f).strip()
else:
    def input(): return sys.stdin.readline().strip()

fprint = lambda *args: print(*args, flush=True)


t = int(input())
for _ in range(t):
    n = int(input())
    a = math.pi / 2 / n
    tmp = 0.5 / math.sin(a)

    print(tmp * math.cos(a / 2) * 2)
