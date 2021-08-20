def __starting_point():
    (n, m) = list(map(int, input().split()))
    matrix = list()
    minR = n
    minC = m
    maxR = maxC = 0
    count = 0
    for i in range(n):
        s = input()
        for j in range(m):
            if s[j] == 'B':
                minR = min(minR, i)
                maxR = max(maxR, i)
                minC = min(minC, j)
                maxC = max(maxC, j)
                count += 1
    edge = max(maxR - minR + 1, maxC - minC + 1)
    if count == 0:
        print(1)
    elif edge > n or edge > m:
        print(-1)
    else:
        print(edge * edge - count)


__starting_point()
