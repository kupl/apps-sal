import math
(n, m, z) = (int(x) for x in input().split())
print(z // (n * m // math.gcd(n, m)))
