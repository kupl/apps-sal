n = int(input())
b = list([list([0, 6, 5]), list([1, 4, 3]), list([8, 2, 7])])
a = list(list())
if n < 3:
    print(-1)
else:
    for i in range(n):
        cur = list()
        for j in range(n):
            cur.append(0)
        a.append(cur.copy())
    val = 1
    for i in range(n - 1, 2, -1):
        if i % 2 == 0:
            for j in range(i + 1):
                a[i][j] = val
                val += 1
            for j in range(i - 1, -1, -1):
                a[j][i] = val
                val += 1
        else:
            for j in range(i + 1):
                a[j][i] = val
                val += 1
            for j in range(i - 1, -1, -1):
                a[i][j] = val
                val += 1
    for i in range(3):
        for j in range(3):
            a[i][j] = val + b[i][j]
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
        print("")
