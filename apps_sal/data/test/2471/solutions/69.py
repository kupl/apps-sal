import numpy as np
from collections import Counter

h, w, n = map(int, input().split())
d = {}
for i in range(n):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1

    am1_f = a - 1 > 0
    ap1_f = a + 1 < h - 1
    bm1_f = b - 1 > 0
    bp1_f = b + 1 < w - 1
    a_f = a > 0 and a < h - 1
    b_f = b > 0 and b < w - 1

    am1 = a - 1
    ap1 = a + 1
    bm1 = b - 1
    bp1 = b + 1

    if am1_f:
        baseid = am1 * w
        if b_f:
            pid = baseid + b

            if pid not in d:
                d[pid] = 1
            else:
                d[pid] += 1

        if bm1_f:
            pid = baseid + bm1
            if pid not in d:
                d[pid] = 1
            else:
                d[pid] += 1

        if bp1_f:
            pid = baseid + bp1
            if pid not in d:
                d[pid] = 1
            else:
                d[pid] += 1

    if ap1_f:
        baseid = ap1 * w
        if b_f:
            pid = baseid + b

            if pid not in d:
                d[pid] = 1
            else:
                d[pid] += 1

        if bm1_f:
            pid = baseid + bm1
            if pid not in d:
                d[pid] = 1
            else:
                d[pid] += 1

        if bp1_f:
            pid = baseid + bp1
            if pid not in d:
                d[pid] = 1
            else:
                d[pid] += 1
    if a_f:

        baseid = a * w
        if b_f:
            pid = baseid + b
            if pid not in d:
                d[pid] = 1
            else:
                d[pid] += 1

        if bm1_f:
            pid = baseid + bm1
            if pid not in d:
                d[pid] = 1
            else:
                d[pid] += 1

        if bp1_f:
            pid = baseid + bp1
            if pid not in d:
                d[pid] = 1
            else:
                d[pid] += 1
    # print(d)

ans = [0 for i in range(10)]

for val in d.values():
    ans[val] += 1

ans[0] = (h - 2) * (w - 2) - sum(ans)

for a in ans:
    print(a)
