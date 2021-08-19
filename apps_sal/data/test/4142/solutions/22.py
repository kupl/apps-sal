S = input()
flag = True
for (i, value) in enumerate(S):
    if i % 2 == 1:
        if value == 'R':
            flag = False
    elif value == 'L':
        flag = False
if flag:
    print('Yes')
else:
    print('No')
