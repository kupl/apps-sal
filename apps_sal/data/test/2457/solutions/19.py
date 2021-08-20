import math
t = int(input())
for _ in range(t):
    (n, a, b, c, d) = list(map(int, input().split()))
    c0 = n * a
    d0 = n * b
    if c0 + d0 < c - d or c0 - d0 > c + d:
        print('No')
    else:
        print('Yes')
