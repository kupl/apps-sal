def main():
    n, m, k = list(map(int, input().split()))
    pipe, res = [], []
    for y in range(1, n + 1):
        for x in list(range(1, m + 1)) if y & 1 else list(range(m, 0, -1)):
            pipe.append(str(y))
            pipe.append(str(x))
    for i in range(0, k * 4 - 4, 4):
        res.append("2 ")
        res.append(' '.join(pipe[i:i + 4]))
        res.append('\n')
    res.append(str(n * m - k * 2 + 2) + ' ')
    res.append(' '.join(pipe[k * 4 - 4:]))
    print(''.join(res))


def __starting_point():
    main()


__starting_point()
