s = input()
L = ['R', 'U', 'D']
M = ['L', 'U', 'D']
lens = len(s)
cnt = 0
for i in range(lens):
    if (i + 1) % 2 == 1 and s[i] in L:
        cnt += 1
    elif (i + 1) % 2 == 0 and s[i] in M:
        cnt += 1
if cnt == lens:
    print('Yes')
else:
    print('No')
