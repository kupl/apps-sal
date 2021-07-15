S = input()

if S[0] == 'A' and S[1].islower() and 'C' in S[2:-1]:
    SS = S.replace('C', '').replace('A', '')
    if SS.islower() and len(SS) == len(S) - 2:
        print('AC')
    else:
        print('WA')
else:
    print('WA')
