from math import *
q = int(input())
for t in range(q):
    n = int(input())
    (a, b, c) = map(int, input().split())
    s = input()
    ans = ['0'] * n
    an = 0
    for i in range(len(s)):
        if s[i] == 'R' and b > 0:
            ans[i] = 'P'
            b -= 1
            an += 1
        if s[i] == 'P' and c > 0:
            ans[i] = 'S'
            c -= 1
            an += 1
        if s[i] == 'S' and a > 0:
            ans[i] = 'R'
            a -= 1
            an += 1
    if an >= (n + 1) // 2:
        print('YES')
        for i in range(len(ans)):
            if ans[i] == '0':
                if a > 0:
                    ans[i] = 'R'
                    a -= 1
                elif b > 0:
                    ans[i] = 'P'
                    b -= 1
                else:
                    ans[i] = 'S'
                    c -= 1
        for i in range(len(ans)):
            print(ans[i], end='')
        print()
    else:
        print('NO')
