import math

a, b, c, d = map(int, input().split())

base = c * d // math.gcd(c, d)

c_num = b // c - (a-1) // c
d_num = b // d - (a-1) // d
base_num = b // base - (a-1) // base

x = int(c_num + d_num - base_num)
print(b-a+1 - x)
