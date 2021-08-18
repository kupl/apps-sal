A, B = list(map(int, input().split()))

if (0 <= A & A <= 23) & (0 <= B & B <= 23):
    if (A + B) > 24:
        print(((A + B) - 24))
    elif (A + B) == 24:
        print((0))
    else:
        print((A + B))
