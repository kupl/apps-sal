from math import gcd
N = int(input())
a = []
ele = 0
for i in range(2, N + 1):
    ele = ele + i
    a.append(ele)
    ele = 0
b = a

lcm = b[0]
for i in b[1:]:
    lcm = lcm * i // gcd(lcm, i)

print(lcm + 1)
