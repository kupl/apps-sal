s = str(input())
num = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
if s[:2] in num and s[2:] in num:
    print('AMBIGUOUS')
elif s[:2] in num:
    print('MMYY')
elif s[2:] in num:
    print('YYMM')
else:
    print('NA')
