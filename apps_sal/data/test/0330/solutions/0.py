import sys
import math

f = sys.stdin

P, Y = list(map(int, f.readline().split()))

is_ok = False
for t in range(Y, P, -1):
    is_ok = True
    for x in range(2, P + 1):
        if t % x == 0:
            is_ok = False
            break
        if x * x > t:
            break
    if is_ok:
        print(t)
        break
if not is_ok:
    print(-1)
