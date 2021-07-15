A, B, C, D = map(int, input().split())
if C>=B or A>=D:
    print(0)
elif C>=A:
    if D >= B:
        print(B-C)
    else:
        print(D-C)
elif A > C:
    if D >= B:
        print(B-A)
    else:
        print(D-A)
