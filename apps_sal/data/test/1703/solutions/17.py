#!/usr/bin/env python3
from sys import stdin, stdout

def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


n = int(input())

s = []
for i in range(n):
    tmp  = input()
    tmp2 = []
    for j in range(len(tmp)):
        if tmp[j] == "(":
            tmp2.append(1)
        else:
            tmp2.append(-1)
    s.append(tmp2)

m =  dict()
for i in range(n):
    # ) : -1, ( : +1
    #)...( : invalid
    if s[i][0] == -1 and s[i][-1] == 1 and len(s[i]) > 2:
        continue
    #)((((()) : for right
    if s[i][-1] ==  -1:
        ss = 0
        flag = 0
        for j in range(len(s[i])-1, -1, -1):
            ss += s[i][j]
            if ss > 0:
                flag = 1
                break
        if flag == 1:
            pass
        else:
            #add to r list
            ss = ss*(-1)
            if not ss in m:
                m[ss] = (0, 1)
            else:
                m[ss] = (m[ss][0], m[ss][1]+1)
    #(((() : for left
    if s[i][0] ==  1:
        ss = 0
        flag = 0
        for j in range(len(s[i])):
            ss += s[i][j]
            if ss < 0:
                flag = 1
                break
        if flag == 1:
            pass
        else:
            if not ss in m:
                m[ss] = (1, 0)
            else:
                m[ss] = (m[ss][0]+1, m[ss][1])
            #add to l list

#print(m)

ans = 0
for mm in m:
    if mm == 0:
        k = m[mm][1]
        ans += k*(k+1) - k
    else:
        #print(m[mm][0], m[mm][1])
        ans +=m[mm][0]*m[mm][1]

print(ans)

