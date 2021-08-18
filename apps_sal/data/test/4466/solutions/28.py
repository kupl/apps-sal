x, y, z = map(int, input().split())
tmp = (x - z) // (y + z)
amari = (x - z) % (y + z)
print(tmp)
