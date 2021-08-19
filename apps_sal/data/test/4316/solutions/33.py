S = sorted(input())
if len(set(S)) == 2 and S[0] == S[1] and (S[1] != S[2]) and (S[2] == S[3]):
    print('Yes')
else:
    print('No')
