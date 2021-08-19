l = int(input())
osy = 0
for i in range(l):
    (n, k) = list(map(int, input().split()))
    if n < k:
        osy = n % 3
        if osy == 0:
            print('Bob')
        else:
            print('Alice')
    else:
        prom = k - 1
        if prom % 3 == 2:
            if n % (k + 1) == k:
                print('Alice')
            elif (n - k) % (k + 1) % 3 == 1:
                print('Bob')
            else:
                print('Alice')
        else:
            osy = n % 3
            if osy == 0:
                print('Bob')
            else:
                print('Alice')
