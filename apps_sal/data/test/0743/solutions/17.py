from fractions import gcd
(n, val) = (int(input()), 0)
for a in (int(x) for x in input().split()):
    val = a if val == 0 else gcd(val, a)
print(val * n)
