a = int(input())
for i in range(a):
    n = int(input())
    l = []
    ls = []
    for i in range(n):
        k = input()
        l.append(k)
        ls.append(k)
    d = list(set(l))
    a = [[0 for i in range(11)] for j in range(5)]
    for i in range(len(d)):
        for j in range(4):
            a[j][int(d[i][j])] = 1
    f = set()
    ans = 0
    ansl = []
    for i in l:
        if i in f:
            r = 0
            ik = 0
            for j in range(10):
                if a[0][j] == 0:
                    a[0][j] = 1
                    r = 1
                    ik = j
                    break
            ansl.append(str(ik) + i[1:])
            ans += 1
            if r == 0:
                r = 0
                ik = 0
                for j in range(10):
                    if a[1][j] == 0:
                        a[1][j] = 1
                        r = 1
                        ik = j
                        break
                ansl.append(i[0] + str(ik) + i[2:])
                ans += 1  
                if r == 0:
                    r = 0
                    ik = 0
                    for j in range(10):
                        if a[2][j] == 0:
                            a[2][j] = 1
                            r = 1
                            ik = j
                            break
                    ansl.append(i[0:2] + str(ik) + i[3:])
                    ans += 1 
                    if r == 0:
                        r = 0
                        ik = 0
                        for j in range(10):
                            if a[3][j] == 0:
                                a[3][j] = 1
                                r = 1
                                ik = j
                                break
                        ansl.append(i[0:-1] + str(ik))
                        ans += 1                     
        else:
            f.add(i)
            ansl.append(i)
    print(ans)
    for i in ansl:
        print(i)

