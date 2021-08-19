import sys
import math
(a, b, c, d) = map(int, sys.stdin.readline().split())
lcm = c * d // math.gcd(c, d)
div_c = b // c - (a - 1) // c
div_d = b // d - (a - 1) // d
div_lcm = b // lcm - (a - 1) // lcm
print(b - a + 1 - div_c - div_d + div_lcm)
