from fractions import gcd
(n, a) = (int(input()), list(map(int, input().split())))
v = a[0]
for ai in a:
    v = gcd(v, ai)
print(v if v in a else -1)
