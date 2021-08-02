for _ in range(int(input())):
    c = int(input())
    f = sorted([int(i) for i in input().split()])
    f1 = False
    ch = 0
    nech = 0
    if f[0] % 2 == 1:
        nech += 1
    else:
        ch += 1
    for i in range(1, c):
        if f[i] - f[i - 1] == 1:
            f1 = True
        if f[i] % 2 == 1:
            nech += 1
        else:
            ch += 1

    if nech % 2 != ch % 2:
        print('NO')
    else:
        if nech % 2 == 0:
            print('YES')
        elif f1:
            print('YES')
        else:
            print('NO')
