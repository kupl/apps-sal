(zlu, blu) = map(int, input().split())
(x, y, z) = map(int, input().split())
zl = 2 * x + y
bl = 3 * z + y
if zl > zlu:
    dif1 = zl - zlu
else:
    dif1 = 0
if bl > blu:
    dif2 = bl - blu
else:
    dif2 = 0
print(dif1 + dif2)
