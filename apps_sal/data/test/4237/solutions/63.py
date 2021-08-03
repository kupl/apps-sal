a, b, c, d = map(int, input().split())
x, y = c, d
while y != 0:
    x, y = y, x % y
lcm = c * d // x
c_upper = b // c
c_lower = -(-a // c)
d_upper = b // d
d_lower = -(-a // d)
lcm_upper = b // lcm
lcm_lower = -(-a // lcm)
print((b - a + 1) - (c_upper - c_lower + 1) - (d_upper - d_lower + 1) + (lcm_upper - lcm_lower + 1))
