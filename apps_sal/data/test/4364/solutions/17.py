s = input()
flag = [0, 0]
if 1 <= int(s[0:2]) <= 12:
    flag[0] = 1
if 1 <= int(s[2:4]) <= 12:
    flag[1] = 1
if flag == [0, 0]:
    print('NA')
if flag == [1, 0]:
    print('MMYY')
if flag == [0, 1]:
    print('YYMM')
if flag == [1, 1]:
    print('AMBIGUOUS')
