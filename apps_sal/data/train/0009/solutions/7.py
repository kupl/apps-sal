from itertools import groupby
t = int(input())
for _ in range(t):
    s = input()
    l = []
    for (k, v) in groupby(s):
        if k == '1':
            l.append(len(list(v)))
    l.sort(reverse=True)
    n = len(l)
    res = 0
    for i in range(0, n, 2):
        res += l[i]
    print(res)
