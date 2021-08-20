(x, y, z) = map(int, input().split())
a = x
x = y
y = a
a = x
x = z
z = a
print(x, y, z)
