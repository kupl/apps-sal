T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    ss = n
    a = []
    while n > 0:
        a.append(n % 3)
        n = n // 3
    fd = -1
    a.append(0)
    p = len(a)
    for i in range(p - 1, -1, -1):
        if a[i] == 2:
            fd = i
            break
    if fd == -1:
        print(ss)
    else:
        for i in range(fd, p):
            if a[i] == 0:
                a[i] = 1
                for j in range(0, i):
                    a[j] = 0
                break
        (ans, k) = (0, 1)
        for i in range(0, p):
            ans += a[i] * k
            k *= 3
        print(ans)
