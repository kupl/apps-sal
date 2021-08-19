YYMM = list(input())
YY = int(YYMM[0] + YYMM[1])
MM = int(YYMM[2] + YYMM[3])
YYMM = False
MMYY = False
if 1 <= MM <= 12:
    YYMM = True
if 1 <= YY <= 12:
    MMYY = True
if YYMM == True and MMYY == True:
    print('AMBIGUOUS')
elif YYMM == True and MMYY == False:
    print('YYMM')
elif YYMM == False and MMYY == True:
    print('MMYY')
elif YYMM == False and MMYY == False:
    print('NA')
