A, B, C, D = map(int, input().split())
if A < C:
    X = C
else:
    X = A
if B < D:
    Y = B
else:
    Y = D
if Y - X < 0:
    print(0)
else:
    print(Y - X)
