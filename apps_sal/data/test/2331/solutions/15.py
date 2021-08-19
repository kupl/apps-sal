from math import gcd
for _ in range(int(input())):
    (a, b) = map(int, input().split())
    print(['Infinite', 'Finite'][gcd(a, b) == 1])
