S = input()

if int(S[2:]) == 0 or int(S[2:]) > 12:
    if int(S[:2]) == 0 or int(S[:2]) > 12:
        print('NA')
    else:
        print('MMYY')
elif int(S[:2]) == 0 or int(S[:2]) > 12:
    print('YYMM')
else:
    print('AMBIGUOUS')
