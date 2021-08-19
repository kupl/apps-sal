import math
import os
import sys
if os.path.exists('/mnt/c/Users/Square/square/codeforces'):
    f = iter(open('D.txt').readlines())

    def input():
        return next(f).strip()
    # input = lambda: sys.stdin.readline().strip()
else:
    def input(): return sys.stdin.readline().strip()

fprint = lambda *args: print(*args, flush=True)


t = int(input())
for _ in range(t):
    n = int(input())
    # print(1.0 / math.tan(math.pi / 2 / n))
    a = math.pi / 2 / n
    tmp = 0.5 / math.sin(a)

    # def func(phi):
    #     return max(math.cos(phi), math.cos(a-phi))

    # l, r = 0, a
    # while l - r > 1e-10:
    #     u = func(l)
    #     v = func(r)
    #     x = func((l*2+r*1)/3)
    #     y = func((l*1+r*2)/3)

    #     if x < y:
    #         r = (l*2+r*1)/3
    #     else:
    #         l = (l*1+r*2)/3
    print(tmp * math.cos(a / 2) * 2)
    # print(n, tmp * func(0))
    # print(tmp * math.cos(0), tmp * math.cos(a-0))
    # print(tmp * func(l))
    # print()
