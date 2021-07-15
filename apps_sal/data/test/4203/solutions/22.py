S = input()
if S[0] == 'A' and 'C' in S[2:-1]:
    idx = S.index('C')
    if all(c.islower() or i in (0, idx) for i, c in enumerate(S)):
        print('AC')
    else:
        print('WA')
else:
    print('WA')
