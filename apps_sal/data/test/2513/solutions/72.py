n = int(input())
s = list(input())
for i in range(4):
    ans = ['?'] * n
    flg = True
# 1,2 = 羊,羊 の場合
    if i == 0:
        ans[0] = 'S'
        ans[1] = 'S'
        if s[0] == 'o':
            ans[-1] = 'S'
        else:
            ans[-1] = 'W'
        if s[1] == 'o':
            if ans[2] == 'W':
                flg = False
            else:
                ans[2] = 'S'
        else:
            if ans[2] == 'S':
                flg = False
            else:
                ans[2] = 'W'
# 1,2 = 羊,狼 の場合
    if i == 1:
        ans[0] = 'S'
        ans[1] = 'W'
        if s[0] == 'o':
            ans[-1] = 'W'
        else:
            ans[-1] = 'S'
        if s[1] == 'o':
            if ans[2] == 'S':
                flg = False
            else:
                ans[2] = 'W'
        else:
            if ans[2] == 'W':
                flg = False
            else:
                ans[2] = 'S'
# 1,2 = 狼,羊 の場合
    if i == 2:
        ans[0] = 'W'
        ans[1] = 'S'
        if s[0] == 'o':
            ans[-1] = 'W'
        else:
            ans[-1] = 'S'
        if s[1] == 'o':
            if ans[2] == 'S':
                flg = False
            else:
                ans[2] = 'W'
        else:
            if ans[2] == 'W':
                flg = False
            else:
                ans[2] = 'S'
# 1,2 = 狼,狼 の場合
    if i == 3:
        ans[0] = 'W'
        ans[1] = 'W'
        if s[0] == 'o':
            ans[-1] = 'S'
        else:
            ans[-1] = 'W'
        if s[1] == 'o':
            if ans[2] == 'W':
                flg = False
            else:
                ans[2] = 'S'
        else:
            if ans[2] == 'S':
                flg = False
            else:
                ans[2] = 'W'
    for i in range(2,n-2):
        if ans[i] == 'S':
            if s[i] == 'o':
                if ans[i-1] == 'S':
                    ans[i+1] = 'S'
                else:
                    ans[i+1] = 'W'
            else:
                if ans[i-1] == 'S':
                    ans[i+1] = 'W'
                else:
                    ans[i+1] = 'S'
        else:
            if s[i] == 'o':
                if ans[i-1] == 'S':
                    ans[i+1] = 'W'
                else:
                    ans[i+1] = 'S'
            else:
                if ans[i-1] == 'S':
                    ans[i+1] = 'S'
                else:
                    ans[i+1] = 'W'
    if ans[-2] == 'S':
        if s[-2] == 'o':
            if ans[-3] != ans[-1]:
                flg = False
        else:
            if ans[-3] == ans[-1]:
                flg = False
    else:
        if s[-2] == 'o':
            if ans[-3] == ans[-1]:
                flg = False
        else:
            if ans[-3] != ans[-1]:
                flg = False
    if ans[-1] == 'S':
        if s[-1] == 'o':
            if ans[-2] != ans[0]:
                flg = False
        else:
            if ans[-2] == ans[0]:
                flg = False
    else:
        if s[-1] == 'o':
            if ans[-2] == ans[0]:
                flg = False
        else:
            if ans[-2] != ans[0]:
                flg = False
    if flg:
        print(''.join(ans))
        return
print(-1)
