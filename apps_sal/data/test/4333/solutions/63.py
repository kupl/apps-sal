X1, Y1, X2, Y2 = map(int, input().split())
a = X2 - X1
b = Y2 - Y1
X3 = X2 - b
Y3 = Y2 + a
X4 = X1 - b
Y4 = Y1 + a
print(X3, end=' ')
print(Y3, end=' ')
print(X4, end=' ')
print(Y4)
