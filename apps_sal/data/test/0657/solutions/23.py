def read():
    return list(map(int, input().split()))


a, b = read()
x, y, z = read()
a -= 2 * x + y
b -= 3 * z + y
s = 0
if a < 0:
    s -= a
if b < 0:
    s -= b
print(s)
