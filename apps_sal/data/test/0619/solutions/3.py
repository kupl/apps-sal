x, y, z = map(int, input().split())
a = x % z
b = y % z
s = x // z + y // z
if a + b >= z:
    print(s + 1, min(z - b, z - a))
else:
    print(s, 0)
