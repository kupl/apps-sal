from decimal import *
import math
getcontext().prec = 100000
(a, b, c) = list(map(int, input().split()))
f = str(Decimal(a) / Decimal(b))
if len(f) < 100000:
    f = f + '0'
suc = False
for i in range(2, 10 ** 5):
    if i == len(f):
        break
    if f[i] == str(c):
        print(i - 1)
        suc = True
        break
if not suc:
    print(-1)
