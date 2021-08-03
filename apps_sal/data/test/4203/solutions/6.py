S = input()
T = S.replace('A', '')
T = T.replace('C', '')
U = T.lower()
if S[0] == 'A' and S.count('A') == 1 and S[2:-1].count('C') == 1 and S.count('C') == 1 and T == U:
    print('AC')
else:
    print('WA')
