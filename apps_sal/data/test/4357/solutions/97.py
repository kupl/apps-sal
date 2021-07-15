a, b, c = map(int, input().split())
X = 10 * a + b + c
Y = a + 10 * b + c
Z = a + b + 10 * c
print(max(X, max(Y, Z)))
