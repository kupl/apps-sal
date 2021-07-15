import math

n = int(input())
tl = [int(input()) for _ in range(n)]

if n == 1:
    print((tl[0]))
else:
    g = tl[0] // math.gcd(tl[0], tl[1]) * tl[1]
    for i in range(1, n):
        g = g // math.gcd(g, tl[i]) * tl[i]
    print(g)

