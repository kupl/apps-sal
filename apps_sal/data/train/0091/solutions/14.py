t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [False] * n
    b[a[0] - 1] = True
    k = 0
    res = [a[0]]
    flag = True
    for j in range(1, n):
        if a[j] == a[j - 1]:
            while k < n and b[k]:
                k += 1
            if k + 1 > a[j]:
                flag = False
                break
            res.append(k + 1)
            b[k] = True
        else:
            b[a[j] - 1] = True
            res.append(a[j])
    if flag:
        print(' '.join(map(str, res)))
    else:
        print(-1)
