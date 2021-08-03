from sys import stdin, stdout
from decimal import *

getcontext().prec = 1000

a, b, c = list(map(int, stdin.readline().rstrip().split()))
x = str(Decimal(a) / Decimal(b))[2:]

if len(x) == 1000:
    x = x[:-1]
else:
    x = ''.join([x, '0'])

if str(c) in x:
    print(x.index(str(c)) + 1)
else:
    print(-1)
