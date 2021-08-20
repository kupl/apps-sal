(a, b) = map(int, input().split())
X = min(a, b)
a = max(0, a - X)
b = max(0, b - X)
Y = a // 2 + b // 2
print(str(X) + ' ' + str(Y))
