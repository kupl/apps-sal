def C2(x):
    if x <= 1:
        return 0
    return x * (x - 1) // 2


def __starting_point():

    n = int(input())
    cake = []
    for i in range(n):
        cake.append([c for c in input()])

    res = 0

    for i in range(n):
        num = 0
        for j in range(n):
            if cake[i][j] == "C":
                num += 1
        res += C2(num)

    for j in range(n):
        num = 0
        for i in range(n):
            if cake[i][j] == "C":
                num += 1
        res += C2(num)

    print(res)


__starting_point()
