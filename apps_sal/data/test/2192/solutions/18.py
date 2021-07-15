def __starting_point():
    n = int(input())
    w = []
    for i in range(n):
        w.append(list(map(int, input().split())))
    a=[]
    b=[]
    for i in range(n):
        a.append([0.0]*n)
        b.append([0.0]*n)
    for i in range(n):
        for j in range(i, n):
            a[i][j] = (w[i][j] + w[j][i]) / 2
            a[j][i] = a[i][j]
            b[i][j] = w[i][j] - a[i][j]
            b[j][i] = w[j][i] - a[j][i]
    for i in range(n):
        print(" ".join(list(map(str, a[i]))))
    for i in range(n):
        print(" ".join(list(map(str, b[i]))))

__starting_point()
