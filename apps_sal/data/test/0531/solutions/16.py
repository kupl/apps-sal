n = int(input())
a = list(map(int, input().split()))
m = min(a)
a = list(map(lambda x: x - m, a))
if max(a) == 1:
    print(n)
    for i in a:
        print(i + m, end=' ')
else:
    (c0, c1, c2) = [0, 0, 0]
    for i in a:
        if i == 0:
            c0 += 1
        elif i == 1:
            c1 += 1
        else:
            c2 += 1
    (ac0, ac1, ac2) = (c0, c1, c2)
    (bc0, bc1, bc2) = (c0, c1, c2)
    t1 = min(ac0, ac2)
    ac1 += 2 * t1
    ac2 -= t1
    ac0 -= t1
    t2 = bc1 - bc1 % 2
    bc2 += t2 // 2
    bc0 += t2 // 2
    bc1 -= t2
    if min(ac1, c1) + min(ac2, c2) + min(ac0, c0) < min(bc1, c1) + min(bc2, c2) + min(bc0, c0):
        print(min(ac1, c1) + min(ac2, c2) + min(ac0, c0))
        out = ''
        for i in range(ac0):
            out += '0 '
        for i in range(ac1):
            out += '1 '
        for i in range(ac2):
            out += '2 '
        for i in out.split():
            print(int(i) + m, end=' ')
    else:
        print(min(bc1, c1) + min(bc2, c2) + min(bc0, c0))
        out = ''
        for i in range(bc0):
            out += '0 '
        for i in range(bc1):
            out += '1 '
        for i in range(bc2):
            out += '2 '
        for i in out.split():
            print(int(i) + m, end=' ')
