for _ in range(int(input())):
    (n, x) = map(int, input().split())
    arr = list(map(int, input().split()))
    a = 0
    b = 0
    for el in arr:
        if el % 2 == 1:
            a += 1
        if el % 2 == 0:
            b += 1
    if a == 0:
        print('No')
        continue
    if x == n:
        if a % 2 == 0:
            print('No')
        else:
            print('Yes')
        continue
    if x % 2 == 0:
        if b == 0:
            print('No')
        else:
            print('Yes')
    else:
        print('Yes')
