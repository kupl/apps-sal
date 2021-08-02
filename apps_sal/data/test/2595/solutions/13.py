for i in range(int(input())):
    a, b = map(int, input().split())
    m = 0
    l = 0
    while a % 2 == 0:
        a //= 2
        m += 1
    while b % 2 == 0:
        b //= 2
        l += 1
    if b != a:
        print(-1)
    else:
        u = abs(l - m)
        if u % 3 != 0:
            print(u // 3 + 1)
        else:
            print(u // 3)
