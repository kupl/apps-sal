import math
X, Y, Z = list(map(int, input().split()))

X -= Z

print((math.floor(X / (Y + Z))))
