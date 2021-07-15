yymm = input()

if (1 <= int(yymm[0:2]) and int(yymm[0:2]) <= 12) and (1 <= int(yymm[2:4]) and int(yymm[2:4]) <= 12):
    print('AMBIGUOUS')
elif (1 <= int(yymm[0:2]) and int(yymm[0:2]) <= 12) and int(yymm[2:4]) <= 99:
    print('MMYY')
elif int(yymm[0:2]) <= 99 and (1 <= int(yymm[2:4]) and int(yymm[2:4]) <= 12):
    print('YYMM')
else:
    print('NA')
