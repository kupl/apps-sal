def aaa():
    n = int(input())
    n *= 2
    a = [[0, 0, 0]] * (n * (n + 1) // 2)
    b = [[]] * n
    used = [-1] * (n + 1)
    for i in range(1, n):
        b[i] = list(map(int, input().split()))
    k = 0
    for i in range(1, n):
        for j in range(i):
            a[k] = [b[i][j], i, j]
            k += 1
    a.sort(reverse=1)
    k = n - 1
    for i in range(k * (k + 1) // 2):
        if used[a[i][1]] == -1 and used[a[i][2]] == -1:
            used[a[i][1]] = a[i][2]
            used[a[i][2]] = a[i][1]
        # print(*used)
    for i in range(n):
        print(used[i] + 1, end=' ')


aaa()
