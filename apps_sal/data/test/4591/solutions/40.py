A, B, C, X, Y = map(int, input().split())
dpr = min(A + B, 2 * C)
Apr = min(A, 2 * C)
Bpr = min(B, 2 * C)

dam = dpr * min(X, Y)
if X >= Y:
    sam = Apr * (X - Y)
else:
    sam = Bpr * (Y - X)

print(dam + sam)
