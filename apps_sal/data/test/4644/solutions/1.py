for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    c1, c2 = 0, 0
    for i in A:
        if i % 2:
            c1 += 1
        else:
            c2 += 1
    if c1 == 0:
        print('NO')
    elif c2 == 0:
        if n% 2:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')


