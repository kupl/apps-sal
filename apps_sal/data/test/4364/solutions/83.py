def check_month(month):
    return 1 <= int(month) <= 12


S = input()
ls = S[:2]
rs = S[2:]
if check_month(ls) and check_month(rs):
    print('AMBIGUOUS')
elif check_month(ls) and (not check_month(rs)):
    print('MMYY')
elif not check_month(ls) and check_month(rs):
    print('YYMM')
else:
    print('NA')
