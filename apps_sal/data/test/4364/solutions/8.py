S = input()

if int(S[:2]) > 12 or int(S[:2]) == 0:
    if int(S[2:]) > 12 or int(S[2:]) == 0:
        print('NA')
    else:
        print('YYMM')
else:
    if int(S[2:]) > 12 or int(S[2:]) == 0:
        print('MMYY')
    else:
        print('AMBIGUOUS')
