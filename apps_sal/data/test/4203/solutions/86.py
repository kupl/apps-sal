S = list(input())

if S[0] == 'A' and S[2:-1].count('C') == 1:
    S.pop(S[2:-1].index('C')+2)
    S.pop(0)
    if ''.join(S) == ''.join(S).lower():
        print('AC')
    else:
        print('WA')
else:
    print('WA')

