a = input()[::-1]
d = ['52', '05', '57']
if len(a) < 2:
    print(-1)
elif a[:2] in d:
    print(0)
else:
    ans = 99999999
    if len([i for i in a if i == '0']) >= 2:
        (x, y) = (-1, -1)
        for i in range(len(a)):
            if a[i] == '0':
                if x < 0:
                    x = i
                elif y < 0:
                    y = i
                else:
                    break
        ans = x + y - 1
    for p in d:
        (x, y) = (-1, -1)
        for i in range(len(a)):
            if a[i] == p[0] and x < 0:
                x = i
            if a[i] == p[1] and y < 0:
                y = i
        if x < 0 or y < 0:
            continue
        c = 0
        if x > y:
            c += 1
            (x, y) = (y, x)
        if y == len(a) - 1 and a[-2] == '0' and (x != len(a) - 2):
            z = -1
            for i in range(len(a) - 1):
                if a[i] != '0' and i != x:
                    z = i
            if z > 0:
                c += len(a) - 2 - z
        c += x + y - 1
        ans = min(ans, c)
    if ans == 99999999:
        ans = -1
    print(ans)
