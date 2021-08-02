for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    ans = a[0] * a[-1]
    b = set(a)
    r = []
    for i in range(2, int(ans**.5 + 1)):
        if ans % i == 0:
            r.append(i)
            r.append(ans // i)
    if set(r) != b:
        print(-1)
    else:
        print(ans)
