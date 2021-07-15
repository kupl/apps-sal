from math import *

zzz = int(input())
for zz in range(zzz):
    n, m = list(map(int, input().split()))
    a = [int(i) for i in input().split()]
    print(int(min(sum(a), m)))

