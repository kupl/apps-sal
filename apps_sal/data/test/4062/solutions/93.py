(a, b, c, d) = map(int, input().split())
x = a * c
y = a * d
z = b * c
w = b * d
n = max(x, y, z, w)
print(n)
