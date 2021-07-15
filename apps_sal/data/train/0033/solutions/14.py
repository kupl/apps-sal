t = int(input())

for _ in range(t):
    n = int(input())

    print(2)
    print('{0} {1}'.format(n-1, n))

    for k in range(n, 2, -1):
        print('{0} {1}'.format(k-2, k))

