from functools import reduce
from operator import *
from math import *
from sys import *
from string import *
setrecursionlimit(10**7)
RI = lambda: list(map(int, input().split()))
RS = lambda: input().rstrip().split()
#################################################
n, m = RI()
ans = 0
while m:
    ans += n // m
    n, m = m, n % m
print(ans)
