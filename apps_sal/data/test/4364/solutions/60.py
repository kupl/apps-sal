S = input()
l = len(S)
Y = 0
M = 0
for i in range(l):
    if i == 3:
        if int(S[i - 1]) == 0 and 1 <= int(S[i]) <= 9:
            Y = 1
        elif int(S[i - 1]) == 1 and 0 <= int(S[i]) <= 2:
            Y = 1
for i in range(l):
    if i == 1:
        if int(S[i - 1]) == 0 and 1 <= int(S[i]) <= 9:
            M = 1
        elif int(S[i - 1]) == 1 and 0 <= int(S[i]) <= 2:
            M = 1
if Y == 1 and M == 1:
    print('AMBIGUOUS')
elif Y == 1 and M == 0:
    print('YYMM')
elif Y == 0 and M == 1:
    print('MMYY')
elif Y == 0 and M == 0:
    print('NA')
