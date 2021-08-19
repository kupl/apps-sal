(A, B) = map(int, input().split())
if A > B:
    print(2 * A - 1)
elif A == B:
    print(A + B)
else:
    print(2 * B - 1)
