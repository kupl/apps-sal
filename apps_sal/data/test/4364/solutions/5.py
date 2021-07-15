s = input()
if s == '0000' or (int(s[:2]) >= 13 and int(s[-2:]) >= 13):
    print('NA')
elif 1 <= int(s[:2]) <= 12 and 1 <= int(s[-2:]) <= 12:
    print('AMBIGUOUS')
elif 1 <= int(s[:2]) <= 12:
    print('MMYY')
elif 1 <= int(s[-2:]) <= 12:
    print('YYMM')
else:
    print('NA')
