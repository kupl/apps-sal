S = int(input())

a = S//100
b = S%100

if 1<=a<=12 and 1<=b<=12:
    print('AMBIGUOUS')
elif 1<=a<=12 and (b>12 or b==0):
    print('MMYY')
elif (a==0 or a>12) and 1<=b<=12:
    print('YYMM')
else:
    print('NA')

