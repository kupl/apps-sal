def __starting_point():
    n = int(input())
    l = list(map(int, input().split()))
    k = []

    for i in range(n - 1, -1, -1):
        if l[i] not in k:
            k.append(l[i])

    k = list(reversed(k))
    print(len(k))
    for i in k:
        print(i, end=' ')


__starting_point()
