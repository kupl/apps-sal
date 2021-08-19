q = int(input())
for _ in range(q):
    (n, k) = map(int, input().split())
    if n == 0:
        print('Bob')
    elif n == 1 or n == 2:
        print('Alice')
    elif n == k:
        print('Alice')
    elif k == 1 or k == 2 or k > n:
        if n % 3 == 0:
            print('Bob')
        else:
            print('Alice')
    elif k % 3 != 0:
        if n % 3 == 0:
            print('Bob')
        else:
            print('Alice')
    else:
        m = n % (k + 1)
        if m % 3 == 0 and m != k:
            print('Bob')
        else:
            print('Alice')
