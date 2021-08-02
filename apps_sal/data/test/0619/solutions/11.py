x, y, z = map(int, input().split())
a = (x + y) // z
xm = x % z
ym = y % z
if x // z + y // z == a:
    ans = 0
else:
    ans = min(z - xm, z - ym)
print((x + y) // z, ans)
