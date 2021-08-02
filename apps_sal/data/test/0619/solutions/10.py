x, y, z = map(int, input().split())

tot = (x + y) // z
min1 = -1
if(x // z + y // z == tot):
    min1 = 0
else:
    min1 = min(z - x % z, z - y % z)
print(tot, min1)
