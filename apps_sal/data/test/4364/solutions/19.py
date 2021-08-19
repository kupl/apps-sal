S = int(input())
L = S // 100
R = S % 100
if 1 <= L <= 12:
    if 1 <= R <= 12:
        print('AMBIGUOUS')
    else:
        print('MMYY')
elif 1 <= R <= 12:
    print('YYMM')
else:
    print('NA')
