A, B, C, X, Y = map(int, input().split())

price = 0

m = min(A + B, C * 2)
n = min(X, Y)
price += m * n

d = max(X, Y) - min(X, Y)
if d != 0:
    if X > Y:
        price += min(A, C * 2) * d
    else:
        price += min(B, C * 2) * d

print(price)
