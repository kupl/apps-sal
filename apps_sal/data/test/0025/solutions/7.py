def maxim():
    (n, k) = list(map(int, input().strip().split()))
    if k < 0:
        print(-1)
        return
    if k > n ** 2:
        print(-1)
        return
    a = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if k >= 1:
            a[i][i] = 1
            k -= 1
        for j in range(i + 1, n):
            if k >= 2:
                a[i][j] = 1
                a[j][i] = 1
                k -= 2
            elif k >= 1:
                break
    if k > 0:
        print(-1)
        return
    for i in range(n):
        b = [str(i) for i in a[i]]
        b = ' '.join(b)
        print(b)


maxim()
