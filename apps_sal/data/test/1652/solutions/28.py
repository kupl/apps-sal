S = input()
last_ind = len(S)
yes = True
for i in range(len(S) - 1, -1, -1):
    if S[i:last_ind] == 'dream' or S[i:last_ind] == 'erase' or S[i:last_ind] == 'eraser' or (S[i:last_ind] == 'dreamer'):
        last_ind = i
        continue
    if last_ind - i > 7 or i == 0:
        yes = False
        break
if yes:
    print('YES')
else:
    print('NO')
