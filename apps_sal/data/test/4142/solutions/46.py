S = input()
ok = True
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == 'L':
            ok = False
            break
    elif S[i] == 'R':
        ok = False
        break
if ok:
    print('Yes')
else:
    print('No')
