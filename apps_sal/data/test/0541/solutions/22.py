def main():
    N, M = list(map(int, input().split()))
    conflict = [tuple(map(int, input().split())) for i in range(M)]
    newest_destroyed = -1
    conflict.sort(key=lambda x: x[1])
    res = 0
    for l, r in conflict:
        if not (l <= newest_destroyed < r):
            res += 1
            newest_destroyed = r - 1
    print(res)
    return


def __starting_point():
    main()


__starting_point()
