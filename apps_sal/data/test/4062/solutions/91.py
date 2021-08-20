(a, b, c, d) = map(int, input().split())
r1 = a * c
r2 = b * d
r3 = a * d
r4 = b * c
print(max(r1, r2, r3, r4))
