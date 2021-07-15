def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

l = input().split(' ')
a, b, c, d = int(l[0]), int(l[1]), int(l[2]), int(l[3])
if a * d > b * c:
    p = a * d - b * c
    q = a * d
else:
    p = b * c - a * d
    q = b * c
e = gcd(p, q)
p //= e
q //= e
print(str(p) + "/" + str(q))

