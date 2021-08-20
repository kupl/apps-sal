q = int(input())
for query in range(q):
    (n, k) = map(int, input().split())
    if k % 3 != 0:
        if n % 3 == 0:
            print('Bob')
        else:
            print('Alice')
    else:
        n = n % (k + 1)
        if n == k:
            print('Alice')
        elif n % 3 == 0:
            print('Bob')
        else:
            print('Alice')
