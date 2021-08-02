s = input()
good = {}
for i in 'abcdefghijklmnopqrstuvwxyz':
    good[i] = 0
for i in s:
    good[i] = 1
s = input()
tmp = s
n = int(input())
for i in range(n):
    q = input()
    while (s[0] == q[0] or (s[0] == '?' and good[q[0]] == 1)):
        s = s[1:]
        q = q[1:]
        if (s == '' or q == ''): break
    if (s != '' and q != ''):
        while (s[-1] == q[-1] or (s[-1] == '?' and good[q[-1]] == 1)):
            s = s[:-1]
            q = q[:-1]
            if (s == '' or q == ''): break
    ans = 1
    if (s == '*'):
        for j in q:
            if (good[j] == 1): ans = 0
    elif (s == q): ans = 1
    else: ans = 0
    if (ans == 1): print("YES")
    else: print("NO")
    s = tmp
