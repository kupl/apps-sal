from math import *
q = int(input())
for t in range(q):
    (a, b) = map(int, input().split())
    c = gcd(a, b)
    if c == 1:
        print('Finite')
    else:
        print('Infinite')
