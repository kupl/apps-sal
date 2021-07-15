s = input()
l = s[:2]
r = s[2:]

if(int(l) >= 1 and int(l) <=12 and int(r) <= 12 and int(r) >= 1):
    print('AMBIGUOUS')
else :
    if(int(l) <= 12 and int(l) >= 1):
        print('MMYY')
    else:
        if(int(r) <= 12 and int(r) >= 1):
            print('YYMM')
        else:
            print('NA')

