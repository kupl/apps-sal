(x, k, d) = map(int, input().split())
an = x
if x < 0:
    x = -x
if k <= x / d:
    an = x - d * k
elif (k - x // d) % 2 == 0:
    an = x - d * (x // d)
else:
    an = x - d * (x // d) - d
print(abs(an))
