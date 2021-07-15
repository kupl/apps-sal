def ex(x, y):
    t = x
    x = y
    y = t
    return x, y


X, Y, Z = list(map(int, input().split()))
X, Y = ex(X, Y)
X, Z = ex(X, Z)

print(f"{X} {Y} {Z}")

