for __ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ar.sort()
    num = 0
    kek = False
    for elem in ar:
        num += elem
        if num == 0:
            kek = True
            break
    if kek:
        ar.sort(reverse=True)
        num = 0
        kek = False
        for elem in ar:
            num += elem
            if num == 0:
                kek = True
                break
        if kek:
            print('NO')
        else:
            print('YES')
            print(*ar)
    else:
        print('YES')
        print(*ar)
