from math import *
for _ in range(int(input())):
    (a, b) = map(int, input().split())
    x = gcd(a, b)
    if x != 1 and a % x == 0 and (b % x == 0):
        print('Infinite')
    else:
        print('Finite')
