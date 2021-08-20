S1 = input()
S2 = input()
if len(S1) == len(S2) and (S1.count('1') == 0 and S2.count('1') == 0 or (S1.count('1') != 0 and S2.count('1') != 0)):
    print('YES')
else:
    print('NO')
