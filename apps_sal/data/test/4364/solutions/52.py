S = list(input())
x = int("".join(S[0:2]))
y = int("".join(S[2:4]))
if 1 <= x <= 12:
    if 1 <= y <= 12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if 1 <= y <= 12:
        print("YYMM")
    else:
        print("NA")
pass
