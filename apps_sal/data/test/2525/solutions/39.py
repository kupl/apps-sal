# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:42:59 2020

@author: liang
"""

from collections import deque
S = deque(input())
Q = int(input())

reverse = False

for i in range(Q):
    t = input().split()
    if int(t[0]) == 1:
        if reverse == False:
            reverse = True
        else:
            reverse = False
    else:
        F = int(t[1])
        C = t[2]
        if F == 1:
            if reverse == False:
                S.appendleft(C)
            else:
                S.append(C)
        else:
            if reverse == False:
                S.append(C)
            else:
                S.appendleft(C)


if reverse == False:
    print((''.join(S)))
else:
    print((''.join(reversed(S))))
