from math import sqrt
a, b = input().split()
c = int(a + b)
d = int(sqrt(c))
print("Yes" if d**2 == c else "No")
