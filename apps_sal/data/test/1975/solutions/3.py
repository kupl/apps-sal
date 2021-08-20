def Comp(n, m):
    count = n + m - 1
    print(str(count))
    print('1 1')
    for i in range(2, m + 1):
        print('1 ' + str(i))
    for i in range(2, n + 1):
        print(str(i) + ' 1')


Comp(*list(map(int, input().split())))
