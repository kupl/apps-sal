(x, y, z) = map(int, input().split())
a = x
b = y
c = z
temp = a
a = b
b = temp
temp = a
a = c
c = temp
print(a, b, c)
