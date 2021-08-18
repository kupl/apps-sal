from math import gcd

n = int(input())

for i in range(n):
    r, b, k = list(map(int, input().split()))
    if r == b:
        print('OBEY')
        continue
    if r < b:
        r, b = b, r
    g = gcd(r, b)
    m = 1 + (r - g - 1) // b
    if m >= k:
        print('REBEL')
    else:
        print('OBEY')
