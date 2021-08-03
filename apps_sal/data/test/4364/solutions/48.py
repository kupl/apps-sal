S = input()

com = ['YYMM', 'MMYY', 'AMBIGUOUS', 'NA']

if 1 <= int(S[:2]) <= 12 and 1 <= int(S[2:]) <= 12:
    print(com[2])
elif 1 <= int(S[:2]) <= 12:
    print(com[1])
elif 1 <= int(S[2:]) <= 12:
    print(com[0])
else:
    print(com[3])
