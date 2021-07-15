import fractions

a, b, c, d = list(map(int, input().split()))
p = max(a * d, b * c) - min(a * d, b * c)
q = max(a * d, b * c)
x = fractions.gcd(p, q)
print(str(p // x) + '/' + str(q // x))

