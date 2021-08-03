for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    k1 = 0
    k2 = 0
    for i in a:
        if i % 2 == 0:
            k1 += 1
        else:
            k2 += 1
    if k1 != 0 and k2 != 0:
        print('NO')
    else:
        print('YES')
