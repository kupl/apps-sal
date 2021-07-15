#589_C

#import time

#start = time.time()

import math

md = (10 ** 9) + 7

def bin(n):
    l = math.floor(math.log(n, 2))
    s = ""
    while l >= 0:
        if n >= 2 ** l:
            n -= 2 ** l
            s += "1"
        else:
            s += "0"
        l -= 1
    return s

def ex(n, m):
    bn = bin(m)
    sm = n
    sms = []
    ssm = 1
    for i in range(len(bn) - 1, -1, -1):
        if bn[i] == "1":
            ssm = (ssm * sm) % md
        sm = (sm * sm) % md
    return ssm

ln = [int(i) for i in input().split(" ")]
x = ln[0]
n = ln[1]

div = []

def pf(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] + pf(n // i)
    return [n]

dv = pf(x)

dv = sorted(dv)

ndv = [[dv[0], 1]]

for i in range(1, len(dv)):
    if dv[i] != dv[i - 1]:
        ndv.append([dv[i], 1])
    else:
        ndv[-1][1] += 1

sm = 1
for i in range(0, len(ndv)):
    nm = math.floor(math.log(n, ndv[i][0])) + 1
    for j in range(1, nm + 1):
        fs = n // (ndv[i][0] ** j)
        if fs == 0:
            continue
        nm = ndv[i][0]

        nn = ex(nm, fs)

        sm = (sm * nn) % md
        #print(sm, i)
print(sm)

