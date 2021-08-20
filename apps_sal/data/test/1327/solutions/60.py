def main():
    import itertools
    (n, m) = list(map(int, input().split()))
    ls = [[] for i in range(8)]
    stats = [stat for stat in itertools.product(*((0, 1) for i in range(3)))]
    for i in range(n):
        (x, y, z) = list(map(int, input().split()))
        for (j, stat) in enumerate(stats):
            ls[j].append(x * (-1) ** stat[0] + y * (-1) ** stat[1] + z * (-1) ** stat[2])
    ans = 0
    for i in range(8):
        a_ = sum(sorted(ls[i], reverse=True)[0:m])
        if a_ > ans:
            ans = a_
    print(ans)


def __starting_point():
    main()


__starting_point()
