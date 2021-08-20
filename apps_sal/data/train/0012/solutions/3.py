from math import *
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt1 = 0
    cnt0 = 0
    cntotr = 0
    f = True
    for i in range(n):
        if a[i] > b[i]:
            if cntotr == 0:
                f = False
                break
        if a[i] < b[i]:
            if cnt1 == 0:
                f = False
                break
        if a[i] == 0:
            cnt0 += 1
        elif a[i] == 1:
            cnt1 += 1
        else:
            cntotr += 1
    if f:
        print('YES')
    else:
        print('NO')
