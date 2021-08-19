(X, Y, Z) = map(int, input().split())
b = Y
c = Z
Y = X
X = b
Z = X
X = c
print(X, Y, Z)
