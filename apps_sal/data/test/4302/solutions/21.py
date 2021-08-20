(A, B) = (int(x) for x in input().split())
if A > B:
    print(2 * A - 1)
elif A < B:
    print(2 * B - 1)
else:
    print(2 * A)
