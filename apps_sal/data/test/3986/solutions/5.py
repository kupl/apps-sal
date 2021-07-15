def main():
    n, k = list(map(int, input().split()))
    if n < k or k == 1 < n:
        print(-1)
    elif (n - k) & 1:
        print('ab' * ((n - k + 1) // 2) + 'acdefghijklmnopqrstuvwxyz'[:k - 1])
    else:
        print('ab' * ((n - k) // 2) + 'abcdefghijklmnopqrstuvwxyz'[:k])


def __starting_point():
    main()

__starting_point()
