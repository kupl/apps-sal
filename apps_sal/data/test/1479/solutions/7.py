def f():
    n, m, k = list(map(int, input().split()))
    a = []
    for i in range(n):
        a.append(list(input().strip()))
    res = [0 for i in range(m)]
    for j in range(m):
        for i in range(1, n):
            if j - i >= 0 and a[i][j - i] == 'R':
                res[j] += 1
            if j + i < m and a[i][i + j] == 'L':
                res[j] += 1
            if i + i < n and a[i + i][j] == 'U':
                res[j] += 1
    print(' '.join(list(map(str, res))))


f()
