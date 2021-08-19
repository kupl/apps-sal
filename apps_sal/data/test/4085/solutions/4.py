import math
for test in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    (x, flag) = (a[0] * a[-1], 0)
    for i in range(len(a)):
        if a[i] * a[-1 - i] != x:
            flag = 1
            break
    if flag == 1:
        print(-1)
        continue
    b = []
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            b.append(i)
            if i != x // i:
                b.append(x // i)
    b = sorted(b)
    if len(a) != len(b):
        print(-1)
        continue
    flag = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            flag = 1
            break
    if flag:
        print(-1)
    else:
        print(x)
