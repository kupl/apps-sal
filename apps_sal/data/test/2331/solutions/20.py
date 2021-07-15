from math import gcd

for __ in range(int(input())):
    a, b = list(map(int, input().split()))
    if gcd(a, b) == 1:
        print('Finite')
    else:
        print('Infinite')
