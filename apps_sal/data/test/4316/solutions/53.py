S = input()
flag = False
if S[0] == S[1] and S[1] != S[2] and S[2] == S[3]:
    flag = True
if S[0] == S[2] and S[2] != S[3] and S[1] == S[3]:
    flag = True
if S[0] == S[3] and S[1] != S[3] and S[1] == S[2]:
    flag = True

if flag:
    print('Yes')
else:
    print('No')
