import math
from collections import Counter, defaultdict
from itertools import accumulate


def R(): return map(int, input().split())


n = int(input())
spl = [math.inf]
ot_forbid = 0
sp = 0
res = 0
for i in range(n):
    arr = list(R())
    tp = arr[0]
    if tp == 1:
        sp = arr[1]
        while sp > spl[-1]:
            spl.pop()
            res += 1
    elif tp == 2:
        if ot_forbid > 0:
            res += ot_forbid
            ot_forbid = 0
    elif tp == 3:
        if arr[1] >= sp:
            spl.append(arr[1])
        else:
            res += 1
    elif tp == 4:
        ot_forbid = 0
    elif tp == 5:
        spl = [math.inf]
    else:
        ot_forbid += 1
print(res)
