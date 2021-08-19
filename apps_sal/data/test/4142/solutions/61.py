S = input()
mistakes = True
for i in range(len(S)):
    tmp = i % 2
    if tmp == 0 and S[i] == 'L':
        mistakes = False
    if tmp == 1 and S[i] == 'R':
        mistakes = False
if mistakes:
    print('Yes')
else:
    print('No')
