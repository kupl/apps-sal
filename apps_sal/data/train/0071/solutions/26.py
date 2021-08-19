import math
t = int(input())
for q in range(t):
    n = int(input())
    P = [int(i) for i in input().split()]
    c = 0
    res = 0
    for i in P:
        if i > 0:
            c += i
        elif i < 0:
            if i < -1 * c:
                res += abs(i + c)
                c = 0
            else:
                c += i
    print(res)
