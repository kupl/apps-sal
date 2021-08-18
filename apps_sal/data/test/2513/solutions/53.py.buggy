n = int(input())
s = list(input())
for i in range(4):
    # 1,2 = 羊,羊 の場合
    ans = ['?'] * n
    flg = True
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
    if flg:
        for i in range(2, n - 1):
            if ans[i] == 'S':
                if s[i] == 'o':
                    if ans[i - 1] == 'S':
                        if ans[i + 1] == 'W':
                            flg = False
                        else:
                            ans[i + 1] = 'S'
                    else:
                        if ans[i + 1] == 'S':
                            flg = False
                        else:
                            ans[i + 1] = 'W'
                else:
                    if ans[i - 1] == 'S':
                        if ans[i + 1] == 'S':
                            flg = False
                        else:
                            ans[i + 1] = 'W'
                    else:
                        if ans[i + 1] == 'W':
                            flg = False
                        else:
                            ans[i + 1] = 'S'
            else:
                if s[i] == 'o':
                    if ans[i - 1] == 'S':
                        if ans[i + 1] == 'S':
                            flg = False
                        else:
                            ans[i + 1] = 'W'
                    else:
                        if ans[i + 1] == 'W':
                            flg = False
                        else:
                            ans[i + 1] = 'S'
                else:
                    if ans[i - 1] == 'S':
                        if ans[i + 1] == 'W':
                            flg = False
                        else:
                            ans[i + 1] = 'S'
                    else:
                        if ans[i + 1] == 'S':
                            flg = False
                        else:
                            ans[i + 1] = 'W'
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
