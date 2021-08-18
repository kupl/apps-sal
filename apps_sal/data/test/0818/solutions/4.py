import math
n = int(input())
s = 0
if n < 3:
    print(-1)
elif n == 3:
    print(210)
else:
    s = 10**(n - 1)
    while 1:
        if s % 2 == 0 and s % 3 == 0 and s % 5 == 0 and s % 7 == 0:
            print(s)
            break
        else:
            s += 1
