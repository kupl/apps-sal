(A, B) = map(int, input().split())
if (A + B) % 2 == 1:
    print((A + B) // 2 + 1)
else:
    print((A + B) // 2)
