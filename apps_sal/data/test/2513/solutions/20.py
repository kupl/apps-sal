n = int(input())
s = input()

for p1, p2 in [(True, True), (True, False), (False, True), (False, False)]:
    ans = []
    ans.extend([p1, p2])
    for i in range(1, n - 1):
        if ans[i] == True:
            if s[i] == 'o':
                ans.append(ans[-2])
            else:
                ans.append(not ans[-2])
        else:
            if s[i] == 'o':
                ans.append(not ans[-2])
            else:
                ans.append(ans[-2])

    f = False
    if ans[-1] == True:
        if s[-1] == 'o' and ans[-2] == ans[0]:
            f = True
        if s[-1] == 'x' and ans[-2] != ans[0]:
            f = True
    else:
        if s[-1] == 'o' and ans[-2] != ans[0]:
            f = True
        if s[-1] == 'x' and ans[-2] == ans[0]:
            f = True

    if f:
        if ans[0] and s[0] == 'o' and ans[1] == ans[-1]:
            break
        if ans[0] and s[0] == 'x' and ans[1] != ans[-1]:
            break
        if not ans[0] and s[0] == 'o' and ans[1] != ans[-1]:
            break
        if not ans[0] and s[0] == 'x' and ans[1] == ans[-1]:
            break
    ans = []

if len(ans) > 0:
    print(''.join(['S' if a else 'W' for a in ans]))
else:
    print(-1)
