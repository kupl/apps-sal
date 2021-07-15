S = input()
point = 0
l = len(S)
i = 0
while i < l:
    if int(i % 2) == 1:
        if S[i] == 'L' or S[i] == 'U' or S[i] == 'D':
            point += 1
    else:
        if S[i] == 'R' or S[i] == 'U' or S[i] == 'D':
            point += 1
    i += 1

if point == l:
    print('Yes')
else:
    print('No')
