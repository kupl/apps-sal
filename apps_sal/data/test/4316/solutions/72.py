S = input()
S2 = list(set(S))

if len(set(S)) == 2 and S.count(S2[0]) == 2 and S.count(S2[1]) == 2:
    print('Yes')
else:
    print('No')
