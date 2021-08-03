s = input()

s_1 = int(s[0:2])
s_2 = int(s[2:4])

if (s_1 > 12 or s_1 < 1) and (s_2 > 12 or s_2 < 1):
    print('NA')
elif s_1 <= 12 and s_1 >= 1 and s_2 <= 12 and s_2 >= 1:
    print('AMBIGUOUS')
elif s_1 <= 12 and s_1 >= 1:
    print('MMYY')
else:
    print('YYMM')
