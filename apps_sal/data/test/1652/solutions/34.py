S = input()

word_lst = ['dream', 'dreamer', 'erase', 'eraser']
for i in range(len(word_lst)):
    word_lst[i] = word_lst[i][::-1]

S = S[::-1]
ans = ''
while len(ans) < len(S) - 4:
    if S[len(ans)] == 'm':
        ans = ans + word_lst[0]
    elif S[len(ans):len(ans) + 3] == 'rem':
        ans = ans + word_lst[1]
    elif S[len(ans)] == 'e':
        ans = ans + word_lst[2]
    elif S[len(ans):len(ans) + 3] == 'res':
        ans = ans + word_lst[3]
    else:
        break

if ans == S:
    print('YES')
else:
    print('NO')
