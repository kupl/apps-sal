def main():
    (n, x) = list(map(int, input().split()))
    s = set(map(int, input().split()))
    res = 0
    for i in range(x):
        if i not in s:
            res += 1
    if x in s:
        res += 1
    print(res)


def __starting_point():
    main()


__starting_point()
