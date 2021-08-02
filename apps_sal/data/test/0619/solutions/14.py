x, y, z = map(int, input().split())
print((x + y) // z, end=" ")
if(x // z + y // z == (x + y) // z):
    print(0)
else:
    print(min(z - x % z, z - y % z))
