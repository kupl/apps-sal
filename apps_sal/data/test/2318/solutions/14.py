n = int(input())
for i in range(n):
    s = input()
    c = input()
    a = []
    b = []
    p = -1
    cnt = 0
    la = 0
    for el in s:
        if p == -1:
            p = el
            cnt += 1
        else:
            if el == p:
                cnt += 1
            else:
                a.append((cnt, p))
                cnt = 1
                la += 1
        p = el
    if cnt != 0:
        a.append((cnt, p))
        la += 1
    p = -1
    cnt = 0
    lb = 0
    for el in c:
        if p == -1:
            p = el
            cnt += 1
        else:
            if el == p:
                cnt += 1
            else:
                b.append((cnt, p))
                cnt = 1
                lb += 1
        p = el
    if cnt != 0:
        b.append((cnt, p))
        lb += 1
    if la != lb:
        print('NO')
        continue
    r = 'YES'
    for i in range(la):
        if a[i][1] != b[i][1] or a[i][0] > b[i][0]:
            r = 'NO'
    print(r)
