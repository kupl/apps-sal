def __starting_point():
    (n, m) = input().split()
    (n, m) = (int(n), int(m))
    d = []
    color = dict()
    for i in range(m):
        d.append(input().split())
    for i in range(len(d)):
        for j in range(len(d[i])):
            d[i][j] = int(d[i][j])
    for i in range(m):
        if i == 0:
            for j in range(3):
                color[d[i][j]] = j + 1
        else:
            temp = dict()
            for j in range(3):
                if d[i][j] in color:
                    temp[color[d[i][j]]] = 1
            for j in range(3):
                if d[i][j] not in color:
                    for k in range(3):
                        if k + 1 not in temp:
                            color[d[i][j]] = k + 1
                            temp[k + 1] = 1
                            break
    for i in range(n):
        print(color[i + 1], end=' ')
    print()


__starting_point()
