def check(a, b):
    ansa = b[0] - a[0]
    ansb = b[1] - a[1]
    return [ansa, ansb]


while True:
    try:
        n, m = map(int, input().split())
        if n != m:
            a = list()
            b = list()
            for i in range(n):
                a.append(list(map(int, input().split())))
            for i in range(m):
                b.append(list(map(int, input().split())))
            print('No')
        else:
            a = list()
            b = list()
            for i in range(n):
                a.append(list(map(int, input().split())))
            for i in range(m):
                b.append(list(map(int, input().split())))
            flag = False
            for i in range(len(a)):
                for j in range(i + 1, len(a)):
                    for k in range(len(b)):
                        for l in range(k + 1, len(b)):
                            ansa = check(a[i], a[j])
                            ansb = check(a[i], b[k])
                            ansc = check(a[i], b[l])
                            if (ansa[0] == ansb[0] and ansa[0] == ansc[0] and ansa[0] == 0) or (ansa[0] != 0 and ansb[0] != 0 and ansc[0] != 0 and ansa[1] / ansa[0] == ansb[1] / ansb[0] and ansa[1] / ansa[0] == ansc[1] / ansc[0]):
                                print('No')
                                flag = True
                                break
                            else:
                                continue
                        if flag == True:
                            break
                    if flag == True:
                        break
                if flag == True:
                    break
            if flag == False:
                print('Yes')
    except EOFError:
        break
