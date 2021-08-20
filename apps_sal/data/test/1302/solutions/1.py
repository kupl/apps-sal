(n, k) = map(int, input().split())
L = [0] * n
if k == n:
    print(-1)
else:
    if (n - (k + 1)) % 2 == 0:
        L[0] = 1
        for i in range(k):
            L[i + 1] = i + 2
        for i in range(k + 1, n, 2):
            L[i] = i + 2
            L[i + 1] = i + 1
    else:
        L[0] = k + 2
        for i in range(k):
            L[i + 1] = i + 2
        for i in range(k + 2, n, 2):
            L[i] = i + 2
            L[i + 1] = i + 1
        L[k + 1] = 1
    print(L[0], end='')
    for i in range(1, n):
        print(' ' + str(L[i]), end='')
