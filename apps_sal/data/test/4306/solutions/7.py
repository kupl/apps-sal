(A, B, C, D) = list(map(int, input().split()))
if A <= C:
    if B <= D:
        if B - C <= 0:
            print(0)
        else:
            print(B - C)
    elif D - C <= 0:
        print(0)
    else:
        print(D - C)
elif B <= D:
    if B - A <= 0:
        print(0)
    else:
        print(B - A)
elif D - A <= 0:
    print(0)
else:
    print(D - A)
