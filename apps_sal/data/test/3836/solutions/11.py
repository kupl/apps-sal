def __starting_point():
    n = int(input())
    supporters = {}
    supporters[0] = []
    supporters[1] = []
    supporters[10] = []
    supporters[11] = []
    for i in range(n):
        [x, y] = [int(x) for x in input().split()]
        supporters[x].append(y)
        # print(x,y)

    for x in supporters:
        supporters[x].sort(reverse=True)
        # print(supporters[x])

    t = 0
    res = 0
    x = len(supporters[11])
    y = len(supporters[10])
    z = len(supporters[1])

    if y > z:
        t = min(x + y, z)
    else:
        t = min(x + z, y)
    k = 0
    for val in supporters[11]:
        res += val
        k += 1

    for i in range(y):
        if i >= t:
            supporters[0].append(supporters[10][i])

        else:
            res += supporters[10][i]
            k += 1
    for i in range(z):
        if i >= t:
            supporters[0].append(supporters[1][i])

        else:
            res += supporters[1][i]
            k += 1

    supporters[0].sort(reverse=True)
    t = min(x + y, x + z)
    i = 0
    # print(res)
    while 2 * t > k and i < len(supporters[0]):
        k += 1
        # print(supporters[0][i])
        res += supporters[0][i]
        i += 1

    print(res)


__starting_point()
