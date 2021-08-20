S = input()
if S[0] == 'A' and S[2:-1].count('C') == 1:
    SC = S.index('C')
    if (S[1:SC] + S[SC + 1:]).islower():
        print('AC')
    else:
        print('WA')
else:
    print('WA')
