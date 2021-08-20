import math
for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    if n < k:
        print('NO')
    elif n % 2 == 0:
        if k % 2 == 0:
            d = []
            for i in range(k - 1):
                d.append(1)
            d.append(n - k + 1)
            print('YES')
            print(*d)
        elif n < 2 * k:
            print('NO')
        else:
            d = []
            for i in range(k - 1):
                d.append(2)
            d.append(n - 2 * (k - 1))
            print('YES')
            print(*d)
    elif k % 2 == 1:
        d = []
        for i in range(k - 1):
            d.append(1)
        d.append(n - k + 1)
        print('YES')
        print(*d)
    else:
        print('NO')
