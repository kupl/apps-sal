a = int(input())
for i in range(a):
    s = input()
    t = input()
    p = input()
    d = dict()
    for x in p:
        d[x] = d.get(x, 0) + 1
    uk1 = 0
    uk = 0
    f = False
    while uk < len(t):
        if uk1 == len(s) and d.get(t[uk], 0) <= 0:
            print('NO')
            f = True
            break
        if uk1 == len(s):
            d[t[uk]] -= 1
            uk += 1
        elif s[uk1] == t[uk]:
            uk += 1
            uk1 += 1
        elif d.get(t[uk], 0) == 0:
            print('NO')
            f = True
            break
        else:
            d[t[uk]] -= 1
            uk += 1
    if not f and uk1 == len(s):
        print('YES')
    elif uk1 != len(s) and not f:
        print('NO')
