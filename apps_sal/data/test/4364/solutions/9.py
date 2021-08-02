S = input()
if 1 <= int(S[0:2]) <= 12:
    if 1 <= int(S[2:4]) <= 12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if 1 <= int(S[2:4]) <= 12:
        print("YYMM")
    else:
        print("NA")
