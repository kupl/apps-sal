# -*- coding: UTF-8 -*-

n, a, b, c, t = list(map(int, input().split()))
msg = [int(x) for x in input().split()]

if b >= c:
    print(a * n)
else:
    ret = 0
    for ti in msg:
        ret += a + (t - ti) * (c - b)
    print(ret)

