N = int(input())
A = [int(a) for a in input().split()]
if N % 2 == 0:
    (x, y, px, py) = (0, 0, 0, -1 << 100)
    for a in A:
        (x, y, px, py) = (px + a, max(x, py + a), x, y)
    print(max(x, y))
else:
    (x, y, z, px, py, pz) = (0, 0, 0, 0, -1 << 100, -1 << 100)
    for a in A:
        (x, y, z, px, py, pz) = (px + a, max(x, py + a), max(y, pz + a), x, y, z)
    print(max(y, z))
