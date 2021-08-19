def __starting_point():
    (n, m) = map(int, input().split())
    total = 0
    for x in range(n):
        data = list(map(int, input().split()))
        total += sum(map(lambda x: min(1, x[0] + x[1]), zip(data[0::2], data[1::2])))
    print(total)


__starting_point()
