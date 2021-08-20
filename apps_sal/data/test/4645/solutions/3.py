t = int(input())
for aoaoao in range(t):
    n = int(input())
    if n == 1:
        print(1)
    elif n < 5:
        if n == 4:
            print('3 1 4 2')
        else:
            print(-1)
    else:
        a = [[], [], [], [], []]
        a[0] = [1, 3, 5, 2, 4]
        a[1] = [1, 3, 5, 2, 6, 4]
        a[2] = [1, 3, 5, 7, 4, 2, 6]
        a[3] = [1, 3, 5, 8, 6, 2, 4, 7]
        a[4] = [1, 3, 5, 9, 7, 4, 2, 6, 8]
        f = -1
        for x in a[n % 5]:
            print(x, end=' ')
        f = max(a[n % 5])
        while f < n:
            for x in a[0]:
                print(f + x, end=' ')
            f += 5
        print()
