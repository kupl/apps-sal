def __starting_point():
    (n, m) = map(int, input().split())
    color = dict()
    for i in range(m):
        d = list(map(int, input().split()))
        temp = dict()
        for j in range(3):
            if d[j] in color:
                temp[color[d[j]]] = 1
        for j in range(3):
            if d[j] not in color:
                for k in range(3):
                    if k + 1 not in temp:
                        color[d[j]] = k + 1
                        temp[k + 1] = 1
                        break
    for i in range(n):
        print(color[i + 1], end=' ')
    print()


__starting_point()
