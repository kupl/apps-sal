a = input()
b = input()
if (len(a) < len(b)):
    q = list(a)
    q.sort(reverse = True)
    print(''.join(q))
else:
    ans = ""
    flag = 0
    while (flag == 0 and len(b) != 0):
        cur = 0
        while (cur < len(a) and a[cur] != b[0]):
            cur += 1
        if (cur < len(a)):
            ans = ans + a[cur]
            a = a[:cur] + a[cur+1:]
            b = b[1:]
        else:
            flag = 1
    if (len(b) == 0):
        print(ans)
    else:
        ma = -1
        p = -1
        for i in range(len(a)):
            if (int(a[i]) > ma and int(a[i]) < int(b[0])):
                ma = int(a[i])
                p = i
        if (ma != -1):
            l = a[p]
            a = a[:p] + a[p+1:]
            q = list(a)
            q.sort(reverse = True)
            print(ans + l + ''.join(q))
        else:
            flag = 0
            while (flag == 0):
                ma = -1
                p = -1
                for i in range(len(a)):
                    if (int(a[i]) > ma and int(a[i]) < int(ans[-1])):
                        ma = int(a[i])
                        p = i
                if (ma != -1):
                    a = a + ans[-1]
                    ans = ans[:-1] + a[p]
                    a = a[:p]+a[p+1:]
                    q = list(a)
                    q.sort(reverse = True)
                    print(ans + ''.join(q))
                    flag = 1
                else:
                    a = a + ans[-1]
                    ans = ans[:-1]


