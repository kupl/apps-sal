S = sorted(input())
if len(set(S)) == 2 and S.count(S[0]) == S.count(S[-1]):
    print('Yes')
else:
    print('No')
