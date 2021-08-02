A, B = map(int, input().split())
if A == B:
    print(2 * A)
else:
    ma = max(A, B)
    print(2 * ma - 1)
