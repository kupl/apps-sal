W, a, b = map(int, input().split())
if a < b:
    A, B = W + a, b
    if A >= B:
        print(0)
    else:
        print(B - A)
else:
    A, B = a, W + b
    if B >= A:
        print(0)
    else:
        print(A - B)
