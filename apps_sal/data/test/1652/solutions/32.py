S = input()
for i in range(100000):
    if S[len(S) - 5:] == 'dream' or S[len(S) - 5:] == 'erase':
        S = S[:len(S) - 5]
    elif S[len(S) - 7:] == 'dreamer':
        S = S[:len(S) - 7]
    elif S[len(S) - 6:] == 'eraser':
        S = S[:len(S) - 6]
    elif S == '':
        print('YES')
        break
    else:
        print('NO')
        break
