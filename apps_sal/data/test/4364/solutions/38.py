S = input()

F = int(S[:2])
B = int(S[2:])

if F == 0 and B == 0:
    print('NA')
elif (F == 0 and B > 12) or (B == 0 and F > 12):
    print('NA')
elif F == 0:
    print('YYMM')
elif B == 0:
    print('MMYY')
elif (F <= 12 and B <= 12):
    print('AMBIGUOUS')
elif F > 12 and B <= 12:
    print('YYMM')
elif F <= 12 and B > 12:
    print('MMYY')
else:
    print('NA')
