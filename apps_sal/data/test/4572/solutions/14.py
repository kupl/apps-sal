import sys
S = list(input())
s = list(set(S))
s.sort()
alfa = list('abcdefghijklmnopqrstuvwxyz')
ans = 0
if(len(s) == len(alfa)):
    print('None')
    return
else:
    for i in range(len(s)):
        if(s[i] != alfa[i]):
            print(alfa[i])
            return
    print(alfa[len(s)])
