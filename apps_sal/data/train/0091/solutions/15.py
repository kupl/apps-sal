t = int(input())
for g in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list((False for i in range(n)))
    flag = False
    count = 0
    res = list(range(n))
    for i in range(n):
        if i == 0:
            res[i] = a[i]
            b[a[i] - 1] = True
        elif a[i] != a[i - 1]:
            res[i] = a[i]
            b[a[i] - 1] = True
        else:
            for j in range(count, n):
                if j + 1 > a[i]:
                    flag = True
                    count = j
                    break
                elif not b[j]:
                    res[i] = j + 1
                    b[j] = True
                    count = j
                    break
    if flag:
        print(-1)
    else:
        for i in range(n):
            print(res[i], end=' ')
        print()
