from sys import stdin
from math import ceil
t = int(stdin.readline().strip())
for caso in range(t):
    n = int(stdin.readline().strip())
    s = list(map(int, stdin.readline().strip().split()))
    s1 = stdin.readline().strip()
    ans = ['' for i in range(n)]
    r = 0
    for i in range(n):
        if s1[i] == 'R' and s[1] > 0:
            ans[i] = 'P'
            s[1] -= 1
            r += 1
        elif s1[i] == 'P' and s[2] > 0:
            ans[i] = 'S'
            r += 1
            s[2] -= 1
        elif s1[i] == 'S' and s[0] > 0:
            ans[i] = 'R'
            r += 1
            s[0] -= 1
    for i in range(n):
        if ans[i] == '':
            if s[0] > 0:
                ans[i] = 'R'
                s[0] -= 1
            elif s[1] > 0:
                ans[i] = 'P'
                s[1] -= 1
            else:
                ans[i] = 'S'
                s[2] -= 1
    if r >= ceil(n / 2):
        print('YES')
        res = ''
        for i in range(n):
            res += ans[i]
        print(res)
    else:
        print('NO')
