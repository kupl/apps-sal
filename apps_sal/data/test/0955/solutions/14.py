import time
max = 300000 + 5
ABC = max
AC = max
AB = max
BC = max
A = max
B = max
C = max
n = int(input())
for i in range(n):
    (c, s) = (i for i in input().split())
    c = int(c)
    if len(s) == 3:
        if c < ABC:
            ABC = c
    elif len(s) == 2:
        if 'A' in s:
            if 'B' in s:
                if c < AB:
                    AB = c
            elif c < AC:
                AC = c
        elif c < BC:
            BC = c
    elif s == 'A':
        if c < A:
            A = c
    elif s == 'B':
        if c < B:
            B = c
    elif c < C:
        C = c
start = time.time()
ans = min(ABC, AB + C, AC + B, BC + A, AB + BC, AB + AC, BC + AC, A + B + C)
if ans == max:
    print(-1)
else:
    print(ans)
finish = time.time()
