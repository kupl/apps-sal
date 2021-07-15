from math import *

def check(a, b, p, s, x):
    ps = s[x]
    ans = 0
    for i in range(x, len(s)):
        if ps == s[i]:
            pass
        else:
            if ps == 'A':
                ans += a
            else:
                ans += b
            if s[i] == 'E':
                break
            ps = s[i]
    return ans <= p

zzz = int(input())
for zz in range(zzz):
    a, b, p = list(map(int, input().split()))
    s = input()
    s = list(s)
    s[-1] = 'E'
    s = ''.join(s)
    lb = 0
    ub = len(s) + 1
    while lb + 1 < ub:
        tx = (lb + ub) // 2
        dx = (ub -lb)//2
        if check(a, b, p, s, tx):
            ub -= dx
        else:
            lb += dx
        #print(ub, lb, dx)

    x = (lb + ub) // 2
    for i in range(4):
        if x > 0 and check(a, b, p, s, x-1):
            x -= 1
        elif x <= len(s) and not check(a, b, p, s, x):
            x += 1
    print(min(x + 1, len(s)))
    

