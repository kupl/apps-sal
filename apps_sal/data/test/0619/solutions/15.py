x, y, z = list(map(int, input().split()))
res1 = (x + y) // z
if x // z + y // z < res1:
    res2 = z - max(x % z, y % z)
else:
    res2 = 0
print(res1, res2)
