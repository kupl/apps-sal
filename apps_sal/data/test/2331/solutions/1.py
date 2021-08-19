from math import gcd
for TT in range(1, int(input()) + 1):
    (a, b) = map(int, input().split())
    print(['Infinite', 'Finite'][gcd(a, b) == 1])
