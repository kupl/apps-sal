a, b, c, d = list(map(int, input().split()))
a = abs(a - c)
b = abs(b - d)

x = min(a, 1) + min(b, 1)
y = max(a, b)
z = 2
if a == b:
    z = 1
if a + b == 0 or (a + b) % 2:
    z = 0

print(x, z, y)
