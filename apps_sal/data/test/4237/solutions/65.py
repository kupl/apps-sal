import math
(a, b, c, d) = map(int, input().split())
e = c * d // math.gcd(c, d)
wa = 0
c_seki = b // c - (a - 1) // c
d_seki = b // d - (a - 1) // d
e_seki = b // e - (a - 1) // e
wa = c_seki + d_seki - e_seki
print(b - a + 1 - wa)
