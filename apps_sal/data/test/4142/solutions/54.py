S = str(input())
flag = True
for i in range(len(S)):
    if i % 2 == 0 and S[i] == 'L':
        flag = False
    elif i % 2 != 0 and S[i] == 'R':
        flag = False
if flag:
    print('Yes')
else:
    print('No')
