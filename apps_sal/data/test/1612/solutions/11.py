def main():
    n = int(input())
    a = [set(map(int, input().split()[1:])) for _ in range(n)]

    res = [True] * n
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i].issubset(a[j]):
                res[j] = False
            if a[i].issuperset(a[j]):
                res[i] = False
    print('\n'.join('YES' if i else 'NO' for i in res))


def __starting_point():
    main()


__starting_point()
