# cook your dish here
from itertools import combinations as c
try:
    n = int(input())
    dt = {}
    x = []
    for _ in range(n):
        t = int(input())
        x.append(t)
        dt[t] = dt.get(t, 0) + 1
    ctr = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            t = x[i] + x[j]
            if t % 2 == 0:
                t >>= 1
                if t in dt:
                    ctr += dt[t]
                    del dt[t]
    print(ctr)
except:
    pass
