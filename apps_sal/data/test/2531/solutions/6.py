# cook your dish here
from itertools import combinations as c
try:
    n = int(input())
    x = []
    odd, even = [], []
    for _ in range(n):
        xx = int(input())
        x.append(xx)
        if xx % 2 == 0:
            even.append(xx)
        else:
            odd.append(xx)
    o = list(c(odd, 2))
    e = list(c(even, 2))
    # print(x,o,e)
    ctr = 0
    dt = {}
    for i in x:
        dt[i] = dt.get(i, 0) + 1
    tt = list(dt.values())
    ctr += sum(tt) - tt.count(1)
    for i in o:
        a, b = i
        if a != b and (a + b) // 2 in x:
            ctr += 1
    for i in e:
        a, b = i
        if a != b and (a + b) // 2 in x:
            ctr += 1
    print(ctr)
except:
    pass
