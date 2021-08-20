S = input()
ans = [0, 0]
if 1 <= int(S[:2]) and int(S[:2]) <= 12:
    ans[0] = 1
if 1 <= int(S[2:]) and int(S[2:]) <= 12:
    ans[1] = 1
if ans == [1, 1]:
    print('AMBIGUOUS')
elif ans == [0, 0]:
    print('NA')
elif ans == [0, 1]:
    print('YYMM')
elif ans == [1, 0]:
    print('MMYY')
