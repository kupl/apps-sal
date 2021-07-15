N = int(input())
s = input()
first = [['S','S'],['S','W'],['W','S'],['W','W']]
flag = 0
mojiretu = ''

def hypothesis(N,s,ans1,ans2):
    ans = [ans1,ans2]
    for i in range(1,N-1):
        if ans[i] == 'S':
            if s[i] == 'o':
                if ans[i-1] == 'S':
                    ans.append('S')
                else:
                    ans.append('W')
            elif s[i] == 'x':
                if ans[i-1] == 'S':
                    ans.append('W')
                else:
                    ans.append('S')
        if ans[i] == 'W':
            if s[i] == 'o':
                if ans[i-1] == 'S':
                    ans.append('W')
                else:
                    ans.append('S')
            elif s[i] == 'x':
                if ans[i-1] == 'S':
                    ans.append('S')
                else:
                    ans.append('W')
    return ans

def conf(ans_sub):
    flag2 = 0
    if ans_sub[0] == 'S' and s[0] == 'o':
        if ans_sub[1] == ans_sub[N-1]:
            if ans_sub[N-1] == 'S' and s[N-1] == 'o':
                if ans_sub[0] == ans_sub[N-2]:
                    flag2 = 1
            elif ans_sub[N-1] == 'S' and s[N-1] == 'x':
                if ans_sub[0] != ans_sub[N-2]:
                    flag2 = 1
            elif ans_sub[N-1] == 'W' and s[N-1] == 'o':
                if ans_sub[0] != ans_sub[N-2]:
                    flag2 = 1
            elif ans_sub[N-1] == 'W' and s[N-1] == 'x':
                if ans_sub[0] == ans_sub[N-2]:
                    flag2 = 1

    elif ans_sub[0] == 'S' and s[0] == 'x':
        if ans_sub[1] != ans_sub[N-1]:
            if ans_sub[N-1] == 'S' and s[N-1] == 'o':
                if ans_sub[0] == ans_sub[N-2]:
                    flag2 = 1
            elif ans_sub[N-1] == 'S' and s[N-1] == 'x':
                if ans_sub[0] != ans_sub[N-2]:
                    flag2 = 1
            elif ans_sub[N-1] == 'W' and s[N-1] == 'o':
                if ans_sub[0] != ans_sub[N-2]:
                    flag2 = 1
            elif ans_sub[N-1] == 'W' and s[N-1] == 'x':
                if ans_sub[0] == ans_sub[N-2]:
                    flag2 = 1

    elif ans_sub[0] == 'W' and s[0] == 'o':
        if ans_sub[1] != ans_sub[N-1]:
            if ans_sub[N-1] == 'S' and s[N-1] == 'o':
                if ans_sub[0] == ans_sub[N-2]:
                    flag2 = 1
            elif ans_sub[N-1] == 'S' and s[N-1] == 'x':
                if ans_sub[0] != ans_sub[N-2]:
                    flag2 = 1
            elif ans_sub[N-1] == 'W' and s[N-1] == 'o':
                if ans_sub[0] != ans_sub[N-2]:
                    flag2 = 1
            elif ans_sub[N-1] == 'W' and s[N-1] == 'x':
                if ans_sub[0] == ans_sub[N-2]:
                    flag2 = 1

    elif ans_sub[0] == 'W' and s[0] == 'x':
        if ans_sub[1] == ans_sub[N-1]:
            if ans_sub[N-1] == 'S' and s[N-1] == 'o':
                if ans_sub[0] == ans_sub[N-2]:
                    flag2 = 1
            elif ans_sub[N-1] == 'S' and s[N-1] == 'x':
                if ans_sub[0] != ans_sub[N-2]:
                    flag2 = 1
            elif ans_sub[N-1] == 'W' and s[N-1] == 'o':
                if ans_sub[0] != ans_sub[N-2]:
                    flag2 = 1
            elif ans_sub[N-1] == 'W' and s[N-1] == 'x':
                if ans_sub[0] == ans_sub[N-2]:
                    flag2 = 1

    if flag2 == 1:
        return 1
    else:
        return 0

for a in first:
    ans_sub = hypothesis(N,s,a[0],a[1])
    flag = conf(ans_sub)
    if flag == 1:
        for x in ans_sub:
            mojiretu += x
        print(mojiretu)
        break
    if flag == 0 and a == first[3]:
        print((-1))

