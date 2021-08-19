(n, k) = list(map(int, input().split(' ')))
if k > n ** 2:
    print(-1)
elif k == n ** 2:
    a = [['1'] * n for i in range(n)]
    for i in range(n):
        a[i] = ' '.join(a[i])
        print(a[i])
else:
    a = [['0'] * n for i in range(n)]
    c = 0
    i = 0
    b = True
    while b and i < n:
        for j in range(n):
            if i == j:
                if c + 1 > k:
                    continue
                a[i][j] = '1'
                c += 1
            elif a[j][i] != '1':
                if c + 2 > k:
                    continue
                a[i][j] = '1'
                a[j][i] = '1'
                c += 2
            if c == k:
                b = False
                break
        i += 1
    for i in range(n):
        a[i] = ' '.join(a[i])
        print(a[i])
