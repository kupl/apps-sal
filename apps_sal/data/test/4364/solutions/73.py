S = input()
if int(S[:2]) == 0 and 0 < int(S[2:]) <= 12:
    print('YYMM')
elif int(S[2:]) == 0 and 0 < int(S[:2]) <= 12:
    print('MMYY')
elif int(S[:2]) == 0 or int(S[2:]) == 0 or (int(S[:2]) > 12 and int(S[2:]) > 12):
    print('NA')
elif int(S[:2]) > 12 and int(S[2:]) <= 12:
    print('YYMM')
elif int(S[:2]) <= 12 and int(S[2:]) > 12:
    print('MMYY')
else:
    print('AMBIGUOUS')
