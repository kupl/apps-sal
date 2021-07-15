s = list(map(int,list(input())))
a = s[0]*10+s[1]
b = s[2]*10+s[3]
if a == 0 and b == 0:
    print('NA')
    return
if 0 < a<= 12 and (b>12 or b==0):
    print('MMYY')
elif (a > 12 or a==0) and 0 < b <= 12:
    print('YYMM')
elif a <= 12 and b <= 12:
    print('AMBIGUOUS')
else:print('NA')
