n = int(input())
a = list(map(int, input().split()))
b = []
o = 0
l = 1
if a[0] == 0:
    f = 0
    for i in range(1, len(a)):
        if a[i] == 0:
            pass
        else:
            if f != 0:
                b += [[l, i]]
                l = i + 1
            f = 1
    if f != 0:
        b += [[l, n]]
else:
    for i in range(1, len(a)):
        if a[i] == 0:
            pass
        else:
            b += [[l, i]]
            l = i + 1
    b += [[l, n]]
if len(b) == 0:
    print('NO')
else:
    print('YES', len(b), sep = '\n')
    for i in b:
        print(*i)

