from math import *

zzz = int(input())
for zz in range(zzz):
    n, m = list(map(int, input().split()))
    print('YES' if n/m == int(n/m)else 'NO' )


