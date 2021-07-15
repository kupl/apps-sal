s = input()
a = 1<= int(s[:2]) <=12
b = 1<= int(s[2:]) <=12
if a and b:
    print("AMBIGUOUS")
elif a:
    print('MMYY')
elif b:
    print('YYMM')
else:
    print('NA')
