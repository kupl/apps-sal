S = input()
T = input()
if S == T:
    print('Yes')
else:
    ans = 'No'
    S = list(S)
    for i in range(len(S)):
        s = S.pop()
        S.insert(0, s)
        if ''.join(S) == T:
            ans = 'Yes'
            break
    print(ans)
