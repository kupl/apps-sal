def readln(): return tuple(map(int, input().split()))

import sys

s = input()
k, = readln()
s += '?' * k

ans = (len(s) // 2) * 2
while ans:
    for i in range(len(s) - ans + 1):
        flag = True
        for j in range(i, i + ans // 2):
            #print(ans, i, j, flag)
            flag = flag and (s[j] == s[j + ans // 2] or s[j + ans // 2] == '?')
        if flag:
            print(ans)
            return
    ans -= 2
