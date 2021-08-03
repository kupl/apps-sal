n = int(input())
if n == 0:
    print('YES')
    print(1)
    print(1)
    print(3)
    print(3)
else:
    lis = []
    for i in range(n):
        lis.append(int(input()))
    lis.sort()

    if n == 1:
        print('YES')
        print(lis[0])
        print(3 * lis[0])
        print(3 * lis[0])

    if n == 2:
        if lis[1] - lis[0] > 2 * lis[0]:
            print('NO')
        else:
            print('YES')
            print(4 * lis[0] - lis[1])
            print(3 * lis[0])
    if n == 3:
        if lis[1] + lis[2] == 4 * lis[0] and max(lis[1], lis[2]) <= 3 * lis[0]:
            print('YES')
            print(3 * lis[0])
        elif lis[2] == 3 * lis[0]:
            print('YES')
            print(4 * lis[0] - lis[1])
        elif (lis[0] + lis[1]) * 3 == 4 * lis[2]:
            print('YES')
            print(int(lis[2] / 3))
        else:
            print('NO')
    if n == 4:
        if lis[3] == 3 * lis[0] and lis[1] + lis[2] == 4 * lis[0]:
            print('YES')
        else:
            print('NO')
