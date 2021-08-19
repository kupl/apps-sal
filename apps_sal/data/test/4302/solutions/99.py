(A, B) = map(int, input().split())
if A == B:
    print(A * 2)
else:
    print(max(A, B) + max(A - 1, B - 1))
