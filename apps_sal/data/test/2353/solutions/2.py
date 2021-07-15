from math import *
from random import *
for t in range(int(input())):
    a, b, c, d = map(int, input().split())
    if b >= a:
        print(b)
        continue
    a -= b
    if d >= c:
        print(-1)
        continue
    otv = b
    cnt = a // (c - d)
    if a % (c - d) != 0:
        cnt += 1
    print(otv + (c * cnt))
