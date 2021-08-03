def wtf(i, k, n):
    if i >= n - k:
        return i
    elif (n - k) % 2 == 0:
        if i % 2 == 0:
            return i + 1
        elif i == 1:
            return 1
        else:
            return i - 1
    else:
        if i % 2 == 0:
            return i - 1
        else:
            return i + 1


def main():
    n, k = list(map(int, input().split()))
    if n == k:
        print(-1)
    else:
        permutation = [str(wtf(i, k, n + 1)) for i in range(1, n + 1)]
        print(" ".join(permutation))


def __starting_point():
    main()


__starting_point()
