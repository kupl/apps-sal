from math import *

def r1(t):
    return t(input().strip())

def r2(t):
    return [t(i) for i in input().strip().split()]

def r3(t):
    return [t(i) for i in input().strip()]

for _ in range(int(input())):
    n, m, x, y = r2(int)
    ans = 0
    cnt = 0
    for i in range(n):
        for j in input():
            if j == '.':
                cnt += 1
                if 2*x <= y:
                    ans += x
                    cnt = 0
                elif cnt == 2:
                    ans += y
                    cnt = 0
            else:
                if cnt == 1:
                    ans += x
                    cnt = 0
        if cnt == 1:
            ans += x
        cnt = 0
        
    print(ans)

