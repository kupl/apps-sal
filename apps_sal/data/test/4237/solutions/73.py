import math
a, b, c, d = map(int, input().split())

cyaku = b // c
dyaku = b // d


cds = b // ((c * d) // (math.gcd(c, d)))

x = b - (cyaku + dyaku - cds)

cyaku2 = (a - 1) // c
dyaku2 = (a - 1) // d

cds2 = (a - 1) // ((c * d) // (math.gcd(c, d)))

y = (a - 1) - (cyaku2 + dyaku2 - cds2)

print(x - y)
