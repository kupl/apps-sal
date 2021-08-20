(x, y, z) = map(int, input().split())
if x % z == 0 or y % z == 0:
    print(x // z + y // z, 0)
else:
    yy = y % z
    xx = x % z
    if yy + xx >= z:
        print(x // z + y // z + 1, min(z - xx, z - yy))
    else:
        print(x // z + y // z, 0)
