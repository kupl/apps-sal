import sys
S = input()
num = len(S)
S = S + "zzzzzzzzzzzzzzzzzzzzzz"
cur = 0
while cur < num:
    if S[cur] == 'd':
        if S[cur:cur+11] == 'dreameraser':
            cur += 11
        elif S[cur:cur+10] == 'dreamerase':
            cur += 10
        elif S[cur:cur+7] == 'dreamer':
            cur += 7
        elif S[cur:cur+5] == 'dream':
            cur += 5
        else:
            print('NO')
            return
    elif S[cur] == 'e':
        if S[cur:cur+6] == 'eraser':
            cur += 6
        elif S[cur:cur+5] == 'erase':
            cur += 5
        else:
            print('NO')
            return
    else:
        print('NO')
        return
    if cur == num:
        print('YES')
        return
