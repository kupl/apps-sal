X, Y = map(int, input().split())
print("Yes" if Y % 2 == 0 and 2 * X <= Y <= 4 * X else "No")
