def cat(h, c):
    return (h * h - c * c) ** 0.5

l3, l4, l5 = list(map(float, input().split()))

s3 = l3 * l3 * 3. ** 0.5 / 4.
s4 = l4 * l4
s5 = (l5 * l5 * (25. + 10 * (5 ** 0.5)) ** 0.5) / 4.

r3 = l3 / (3. ** 0.5)
r4 = l4 / (2. ** 0.5)
r5 = l5 / 10. * (10. ** 0.5 * (5. + 5. ** 0.5) ** 0.5)

h3 = cat(l3, r3)
h4 = cat(l4, r4)
h5 = cat(l5, r5)

v3 = s3 * h3 / 3.
v4 = s4 * h4 / 3.
v5 = s5 * h5 / 3.
print(v3 + v4 + v5)


