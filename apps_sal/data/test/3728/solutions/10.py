n, m = list(map(int, input().split()))

def f(a):
    nonlocal c, k
    c = []
    k = 0
    for i in range(m):
        if a[i] - 1 != i:
            k += 1
            c.append(i)
    
            

c = []
bb = []
cc = []
k = 0
flag1 = True
flag = True
for i in range(n):
    b = list(map(int, input().split()))
    f(b)
    if k > 2:
        flag1 = False
    if k > 2:
        if k > 4:
            print('NO')
            flag = False
            break
        elif cc == []:
            for j in range(len(c)):
                cc.append(c[j])
        elif k == 3:
            cc = []
            for j in range(len(c)):
                cc.append(c[j])
    bb.append(b)
if flag1:
    print('YES')
else:
    if flag:
        for i in range(n):
            bb[i][cc[0]], bb[i][cc[1]] = bb[i][cc[1]], bb[i][cc[0]]
            f(bb[i])
            if k > 2:
                flag = False
            bb[i][cc[0]], bb[i][cc[1]] = bb[i][cc[1]], bb[i][cc[0]]
        if flag:
            print('YES')
        else:
            flag = True
            for i in range(n):
                bb[i][cc[0]], bb[i][cc[2]] = bb[i][cc[2]], bb[i][cc[0]]
                f(bb[i])
                if k > 2:
                    flag = False
                bb[i][cc[0]], bb[i][cc[2]] = bb[i][cc[2]], bb[i][cc[0]]
            if flag:
                print('YES')
            else:
                flag = True
                for i in range(n):
                    bb[i][cc[1]], bb[i][cc[2]] = bb[i][cc[2]], bb[i][cc[1]]
                    f(bb[i])
                    if k > 2:
                        flag = False
                    bb[i][cc[1]], bb[i][cc[2]] = bb[i][cc[2]], bb[i][cc[1]]
                if flag:
                    print('YES')
                else:
                    if len(cc) == 3:
                        print('NO')
                    else:
                        flag = True
                        for i in range(n):
                            bb[i][cc[0]], bb[i][cc[3]] = bb[i][cc[3]], bb[i][cc[0]]
                            f(bb[i])
                            if k > 2:
                                flag = False
                            bb[i][cc[0]], bb[i][cc[3]] = bb[i][cc[3]], bb[i][cc[0]]
                        if flag:
                            print('YES')
                        else:
                            flag = True
                            for i in range(n):
                                bb[i][cc[1]], bb[i][cc[3]] = bb[i][cc[3]], bb[i][cc[1]]
                                f(bb[i])
                                if k > 2:
                                    flag = False
                                bb[i][cc[1]], bb[i][cc[3]] = bb[i][cc[3]], bb[i][cc[1]]
                            if flag:
                                print('YES')
                            else:
                                flag = True
                                for i in range(n):
                                    bb[i][cc[2]], bb[i][cc[3]] = bb[i][cc[3]], bb[i][cc[2]]
                                    f(bb[i])
                                    if k > 2:
                                        flag = False
                                    bb[i][cc[2]], bb[i][cc[3]] = bb[i][cc[3]], bb[i][cc[2]]
                                if flag:
                                    print('YES')
                                else:
                                    print('NO')

                              

