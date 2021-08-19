(a, b, c, d) = (int(x) for x in input().split())
ac = a * c
ad = a * d
bc = b * c
bd = b * d
q = [ac, ad, bc, bd]
high = q[0]
for value in q:
    if value > high:
        high = value
print(high)
