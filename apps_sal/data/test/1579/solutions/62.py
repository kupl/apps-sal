def main():
    MAX = 10 ** 5 + 1

    data = [-1] * (2 * MAX)

    def find(x):
        if data[x] < 0:
            return x
        else:
            data[x] = find(data[x])
            return data[x]

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            if data[y] < data[x]:
                x, y = y, x
            data[x] += data[y]
            data[y] = x
        return (x != y)


    N, *XY = list(map(int, open(0).read().split()))

    for x, y in zip(*[iter(XY)] * 2):
        union(x, y + MAX)

    X = [0] * (MAX * 2)
    Y = [0] * (MAX * 2)

    for i in range(MAX):
        X[find(i)] += 1
    for i in range(MAX, MAX * 2):
        Y[find(i)] += 1

    res = sum(X[i] * Y[i] for i in range(MAX * 2))

    print((res - N))


def __starting_point():
    main()

__starting_point()
