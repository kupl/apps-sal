n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
matr = [[(), (), (), ()], [(), (), (), ()], [(), (), (), ()], [(), (), (), ()]]
matr[0][0] = (0, 0)
matr[0][1] = (-1, -1)
matr[0][2] = (-1, -1)
matr[0][3] = (-1, -1)
matr[1][0] = (1, 0)
matr[1][1] = (1, 1)
matr[1][2] = (-1, -1)
matr[1][3] = (-1, -1)
matr[2][0] = (2, 0)
matr[2][1] = (-1, -1)
matr[2][2] = (2, 2)
matr[2][3] = (-1, -1)
matr[3][1] = (1, 3)
matr[3][2] = (3, 2)
matr[3][3] = (3, 3)
t = []
if (a[0] != 3 or b[0] != 0) and matr[a[0]][b[0]][0] == -1:
    print('NO')
    return
else:
    if a[0] == 3 and b[0] == 0:
        t.append(3)
        t.append(0)
        f = False
        for i in range(1, n - 1):
            if a[i] == 3 and b[i] == 0:
                if t[i] == 0:
                    t.append(3)
                elif t[i] == 1:
                    t.append(2)
                elif t[i] == 2:
                    t.append(1)
                else:
                    t.append(0)
            elif matr[a[i]][b[i]][0] != t[i] and matr[a[i]][b[i]][1] != t[i]:
                f = True
                break
            else:
                if matr[a[i]][b[i]][0] == t[i]:
                    t.append(matr[a[i]][b[i]][1])
                else:
                    t.append(matr[a[i]][b[i]][0])
        if not f:
            print('YES')
            print(*t)
        else:
            t = []
            t.append(0)
            t.append(3)
            f = False
            for i in range(1, n - 1):
                if a[i] == 3 and b[i] == 0:
                    if t[i] == 0:
                        t.append(3)
                    elif t[i] == 1:
                        t.append(2)
                    elif t[i] == 2:
                        t.append(1)
                    else:
                        t.append(0)
                elif matr[a[i]][b[i]][0] != t[i] and matr[a[i]][b[i]][1] != t[i]:
                    f = True
                    break
                else:
                    if matr[a[i]][b[i]][0] == t[i]:
                        t.append(matr[a[i]][b[i]][1])
                    else:
                        t.append(matr[a[i]][b[i]][0])
            if not f:
                print('YES')
                print(*t)
            else:
                t = []
                t.append(1)
                t.append(2)
                f = False
                for i in range(1, n - 1):
                    if a[i] == 3 and b[i] == 0:
                        if t[i] == 0:
                            t.append(3)
                        elif t[i] == 1:
                            t.append(2)
                        elif t[i] == 2:
                            t.append(1)
                        else:
                            t.append(0)
                    elif matr[a[i]][b[i]][0] != t[i] and matr[a[i]][b[i]][1] != t[i]:
                        f = True
                        break
                    else:
                        if matr[a[i]][b[i]][0] == t[i]:
                            t.append(matr[a[i]][b[i]][1])
                        else:
                            t.append(matr[a[i]][b[i]][0])
                if not f:
                    print('YES')
                    print(*t)
                else:
                    t = []
                    t.append(2)
                    t.append(1)
                    f = False
                    for i in range(1, n - 1):
                        if a[i] == 3 and b[i] == 0:
                            if t[i] == 0:
                                t.append(3)
                            elif t[i] == 1:
                                t.append(2)
                            elif t[i] == 2:
                                t.append(1)
                            else:
                                t.append(0)
                        elif matr[a[i]][b[i]][0] != t[i] and matr[a[i]][b[i]][1] != t[i]:
                            f = True
                            break
                        else:
                            if matr[a[i]][b[i]][0] == t[i]:
                                t.append(matr[a[i]][b[i]][1])
                            else:
                                t.append(matr[a[i]][b[i]][0])
                    if not f:
                        print('YES')
                        print(*t)
                    else:
                        print('NO')
    else:
        t.append(matr[a[0]][b[0]][0])
        t.append(matr[a[0]][b[0]][1])
        f = False
        for i in range(1, n - 1):
            if a[i] == 3 and b[i] == 0:
                if t[i] == 0:
                    t.append(3)
                elif t[i] == 1:
                    t.append(2)
                elif t[i] == 2:
                    t.append(1)
                else:
                    t.append(0)
            elif matr[a[i]][b[i]][0] != t[i] and matr[a[i]][b[i]][1] != t[i]:
                f = True
                break
            else:
                if matr[a[i]][b[i]][0] == t[i]:
                    t.append(matr[a[i]][b[i]][1])
                else:
                    t.append(matr[a[i]][b[i]][0])
        if not f:
            print('YES')
            print(*t)
        else:
            t = []
            t.append(matr[a[0]][b[0]][1])
            t.append(matr[a[0]][b[0]][0])
            f = False
            for i in range(1, n - 1):
                if a[i] == 3 and b[i] == 0:
                    if t[i] == 0:
                        t.append(3)
                    elif t[i] == 1:
                        t.append(2)
                    elif t[i] == 2:
                        t.append(1)
                    else:
                        t.append(0)
                elif matr[a[i]][b[i]][0] != t[i] and matr[a[i]][b[i]][1] != t[i]:
                    f = True
                    break
                else:
                    if matr[a[i]][b[i]][0] == t[i]:
                        t.append(matr[a[i]][b[i]][1])
                    else:
                        t.append(matr[a[i]][b[i]][0])
            if not f:
                print('YES')
                print(*t)
            else:
                print('NO')

