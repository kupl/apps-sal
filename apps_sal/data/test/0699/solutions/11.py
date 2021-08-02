from functools import reduce
from operator import *
from math import *
from sys import *
setrecursionlimit(10**7)
RI = lambda: list(map(int, input().split()))
RS = lambda: input().rstrip().split()
#################################################
y, k, n = RI()
st = k - y % k
if st + y > n:
    print(-1)
else:
    while 1:
        if st + y > n:
            break
        print(st, end=" ")
        st += k
