from math import *
from sys import *
input = stdin.readline

for _ in range(1):

    n = int(input())
    a = list(map(int, input().split()))

    d = {0: 1}
    cn = 0

    sn = 0
    for i in range(n):
        sn += a[i]
        if(d.get(sn, 0) == 1):
            sn = a[i]
            cn += 1
            d = {0: 1, a[i]: 1}
        else:
            d[sn] = 1

    stdout.write(str(cn) + '\n')
