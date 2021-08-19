S = str(input())
T = [S[0], S[1], S[2], S[3]]
T.sort()
if T[0] == T[1] and T[2] == T[3] and (T[1] != T[2]):
    print('Yes')
else:
    print('No')
