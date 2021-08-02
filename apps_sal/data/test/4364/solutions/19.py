S = int(input())

L = S // 100  # 前半2桁
R = S % 100  # 後半2桁

if 1 <= L <= 12:
    if 1 <= R <= 12: print('AMBIGUOUS')
    else: print('MMYY')
else:
    if 1 <= R <= 12: print('YYMM')
    else: print('NA')
