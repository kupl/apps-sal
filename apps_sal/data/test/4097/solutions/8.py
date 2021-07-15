n = int(input())
a = list(map(int, input().split()))

if n == 1 or n == 2:
    print(0)
else:
    diff = [a[1] - a[0], a[1] + 1 - a[0], a[1] - 1 - a[0],
            a[1] - a[0] + 1, a[1] + 1 - a[0] + 1, a[1] - 1 - a[0] + 1,
            a[1] - a[0] - 1, a[1] + 1 - a[0] - 1, a[1] - 1 - a[0] - 1]

    flag1 = False
    num = float("inf")
    flag = True
    pre = a[1]
    d = diff[0]
    rec = 0
    for j in range(2, n):
        if a[j] - pre == d + 1:
            rec += 1
            pre = a[j] - 1
        elif a[j] - pre == d - 1:
            rec += 1
            pre = a[j] + 1
        elif a[j] - pre == d:
            pre = a[j]
        else:
            flag = False
            break

    if flag:
        flag1 = True
        num = min(num, rec)

    flag = True
    pre = a[1] + 1
    d = diff[1]
    rec = 1
    for j in range(2, n):
        if a[j] - pre == d + 1:
            rec += 1
            pre = a[j] - 1
        elif a[j] - pre == d - 1:
            rec += 1
            pre = a[j] + 1
        elif a[j] - pre == d:
            pre = a[j]
        else:
            flag = False
            break

    if flag:
        flag1 = True
        num = min(num, rec)

    flag = True
    pre = a[1] - 1
    d = diff[2]
    rec = 1
    for j in range(2, n):
        if a[j] - pre == d + 1:
            rec += 1
            pre = a[j] - 1
        elif a[j] - pre == d - 1:
            rec += 1
            pre = a[j] + 1
        elif a[j] - pre == d:
            pre = a[j]
        else:
            flag = False
            break

    if flag:
        flag1 = True
        num = min(num, rec)

    flag = True
    pre = a[1]
    d = diff[3]
    rec = 1
    for j in range(2, n):
        if a[j] - pre == d + 1:
            rec += 1
            pre = a[j] - 1
        elif a[j] - pre == d - 1:
            rec += 1
            pre = a[j] + 1
        elif a[j] - pre == d:
            pre = a[j]
        else:
            flag = False
            break

    if flag:
        flag1 = True
        num = min(num, rec)

    flag = True
    pre = a[1] + 1
    d = diff[4]
    rec = 2
    for j in range(2, n):
        if a[j] - pre == d + 1:
            rec += 1
            pre = a[j] - 1
        elif a[j] - pre == d - 1:
            rec += 1
            pre = a[j] + 1
        elif a[j] - pre == d:
            pre = a[j]
        else:
            flag = False
            break

    if flag:
        flag1 = True
        num = min(num, rec)

    flag = True
    pre = a[1] - 1
    d = diff[5]
    rec = 2
    for j in range(2, n):
        if a[j] - pre == d + 1:
            rec += 1
            pre = a[j] - 1
        elif a[j] - pre == d - 1:
            rec += 1
            pre = a[j] + 1
        elif a[j] - pre == d:
            pre = a[j]
        else:
            flag = False
            break

    if flag:
        flag1 = True
        num = min(num, rec)

    flag = True
    pre = a[1]
    d = diff[6]
    rec = 1
    for j in range(2, n):
        if a[j] - pre == d + 1:
            rec += 1
            pre = a[j] - 1
        elif a[j] - pre == d - 1:
            rec += 1
            pre = a[j] + 1
        elif a[j] - pre == d:
            pre = a[j]
        else:
            flag = False
            break

    if flag:
        flag1 = True
        num = min(num, rec)

    flag = True
    pre = a[1] + 1
    d = diff[7]
    rec = 2
    for j in range(2, n):
        if a[j] - pre == d + 1:
            rec += 1
            pre = a[j] - 1
        elif a[j] - pre == d - 1:
            rec += 1
            pre = a[j] + 1
        elif a[j] - pre == d:
            pre = a[j]
        else:
            flag = False
            break

    if flag:
        flag1 = True
        num = min(num, rec)

    flag = True
    pre = a[1] - 1
    d = diff[8]
    rec = 2
    for j in range(2, n):
        if a[j] - pre == d + 1:
            rec += 1
            pre = a[j] - 1
        elif a[j] - pre == d - 1:
            rec += 1
            pre = a[j] + 1
        elif a[j] - pre == d:
            pre = a[j]
        else:
            flag = False
            break

    if flag:
        flag1 = True
        num = min(num, rec)

    if flag1:
        print(num)
    else:
        print(-1)
