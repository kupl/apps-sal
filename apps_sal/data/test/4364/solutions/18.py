S = input()
S_f = S[:2]
S_b = S[2:]
com = ['YYMM', 'MMYY', 'AMBIGUOUS', 'NA']
if 1 <= int(S_f) <= 12:
    if 1 <= int(S_b) <= 12:
        print(com[2])
    else:
        print(com[1])
elif 1 <= int(S_b) <= 12:
    if 1 <= int(S_f) <= 12:
        print(com[2])
    else:
        print(com[0])
else:
    print(com[3])
