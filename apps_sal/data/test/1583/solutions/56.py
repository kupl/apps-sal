from math import*
A, B, X = map(int, input().split())
V = A * A * B

if V / 2 < X:
    print(degrees(atan(2 * (V - X) / A**3)))
else:
    print(degrees(atan(A * B * B / 2 / X)))
