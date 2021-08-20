S = input()
if S.count('R') == 3 or S.count('R') == 1 or S.count('R') == 0:
    print(S.count('R'))
elif S[0] == S[2]:
    print('1')
else:
    print('2')
