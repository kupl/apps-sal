(A, B) = map(int, input().split())
if A + B > 23:
    print((A + B) % 24)
else:
    print(A + B)
