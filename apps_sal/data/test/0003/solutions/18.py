def __starting_point():
    (N, Q) = list(map(int, input().strip().split()))
    painters = []
    for i in range(Q):
        painters.append(tuple(map(int, input().strip().split())))
    C = [[] for i in range(N + 1)]
    for i in range(len(painters)):
        (start, end) = painters[i]
        for j in range(start, end + 1):
            C[j].append(i)
    C = C[1:]
    total = sum((1 for i in C if len(i) > 0))
    count = [[0 for i in range(Q)] for j in range(Q)]
    for i in range(N):
        if len(C[i]) == 2:
            count[C[i][0]][C[i][1]] += 1
            count[C[i][1]][C[i][0]] += 1
        if len(C[i]) == 1:
            for j in range(Q):
                if j != C[i][0]:
                    count[C[i][0]][j] += 1
                    count[j][C[i][0]] += 1
    mini = 100000
    for i in range(Q):
        for j in range(Q):
            if i != j and count[i][j] < mini:
                mini = count[i][j]
    print(total - mini)


__starting_point()
