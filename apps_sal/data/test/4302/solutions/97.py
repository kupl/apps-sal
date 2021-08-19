(A, B) = map(int, input().split())
if A == B:
    print(A + B)
else:
    print(2 * max(A, B) - 1)
