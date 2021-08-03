A, B, C, X, Y = map(int, input().split())

ab = min(2 * C, A + B)
a = min(2 * C, A)
b = min(2 * C, B)

if X <= Y:
    ans = X * ab + (Y - X) * b
else:
    ans = Y * ab + (X - Y) * a
print(ans)
