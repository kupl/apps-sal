from collections import Counter


def main():
    n = int(input())
    a = Counter(list(map(int, input().split())))

    res = [0] * len(a)
    _i = 0
    for j, (i, cnt) in enumerate(sorted(list(a.items()), reverse=True)):
        if i == _i - 1:
            res[j] = max(res[j - 1], res[j - 2] + i * a[i])
        else:
            res[j] = res[j - 1] + i * a[i]
        _i = i

    print(res[-1])


def __starting_point():
    main()


__starting_point()
