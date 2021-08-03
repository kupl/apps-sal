from math import sqrt
a, b = map(str, input().split())
print("Yes" if sqrt(int(a + b)) == int(sqrt(int(a + b))) else "No")
