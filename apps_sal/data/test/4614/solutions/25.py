A, B, C = list(map(int, input().split()))

if A - B == 0:
    print(C)
elif A - C == 0:
    print(B)
else:
    print(A)

