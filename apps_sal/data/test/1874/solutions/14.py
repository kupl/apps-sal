from math import sqrt as s
(x, y, z) = map(int, input().split())
print(pow(x, 3) * (1 / 6 / s(2)) + pow(y, 3) * (s(2) / 6) + pow(z, 3) * ((5 + s(5)) / 24))
