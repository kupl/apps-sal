S = input()
S_front = S[:2]
S_back = S[2:]

if 0 < int(S_front) < 13:
    if 0 < int(S_back) < 13:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if 0 < int(S_back) < 13:
        print("YYMM")
    else:
        print("NA")
