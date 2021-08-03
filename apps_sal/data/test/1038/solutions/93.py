A, B = map(int, input().split())

if (A % 2 == 0) and (B % 2 == 0):
    if (B - A) % 4 == 0:
        print(B)
    else:
        print(B + 1)
elif (A % 2 == 0) and (B % 2 == 1):
    if (B - A + 1) % 4 == 0:
        print(0)
    else:
        print(1)
elif (A % 2 == 1) and (B % 2 == 0):
    if (B - A - 1) % 4 == 0:
        print(A ^ B)
    else:
        print(A ^ B ^ 1)
else:
    if (B - A) % 4 == 0:
        print(A)
    else:
        print(A ^ 1)
