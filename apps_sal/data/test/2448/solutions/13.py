'''
Created on 2019. 9. 21.

@author: kkhh88
'''

import math
q = int(input())
for _ in range(q):
    n = int(input())
    a, b, c = map(int, input().split(' '))

    bob = input()
    alice = ['X'] * n

    cnt = 0
    for i in range(n):
        s = bob[i]
        if s == 'R' and b > 0:
            b = b - 1
            cnt = cnt + 1
            alice[i] = 'P'
        elif s == 'P' and c > 0:
            c = c - 1
            cnt = cnt + 1
            alice[i] = 'S'
        elif s == 'S' and a > 0:
            a = a - 1
            cnt = cnt + 1
            alice[i] = 'R'

    if (n + 1) // 2 <= cnt:
        win = ''
        for i in range(n):
            if alice[i] == 'X':
                if a > 0:
                    a = a - 1
                    win = win + 'R'
                elif b > 0:
                    b = b - 1
                    win = win + 'P'
                elif c > 0:
                    c = c - 1
                    win = win + 'S'
            else:
                win = win + alice[i]
        print("YES")
        print(win)
    else:
        print("NO")
