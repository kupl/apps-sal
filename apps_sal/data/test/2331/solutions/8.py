from math import *
q = int(input())
for i in range(q):
    (a, b) = map(int, input().split())
    if gcd(a, b) == 1:
        print('Finite')
    else:
        print('Infinite')
