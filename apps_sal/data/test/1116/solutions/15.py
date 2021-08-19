from math import gcd
t = int(input())
for i in range(t):
    (r, b, k) = [int(x) for x in input().split()]
    if b > r:
        (b, r) = (r, b)
    g = gcd(r, b)
    c = (r - g - 1) // b + 1
    if c >= k:
        print('REBEL')
    else:
        print('OBEY')
