S = input()
c = 1
if S[0] == S[1]:
    if S[2] == S[3] and S[0] != S[2]:
        c = 0

elif S[0] == S[2]:
    if S[1] == S[3] and S[0] != S[1]:
        c = 0

elif S[0] == S[3]:
    if S[1] == S[2] and S[0] != S[1]:
        c = 0


if c:
    print('No')

else:
    print('Yes')
