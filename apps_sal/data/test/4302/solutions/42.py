A, B = map(int, input().split())

if A == B:
    print(2 * A)
else:
    print(max(A, B) + max(A, B) - 1)
