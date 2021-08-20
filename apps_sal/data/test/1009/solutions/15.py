def main():
    (n, k) = map(int, input().split())
    s = list(map(int, input().split()))
    minSize = s[n - 1]
    if n <= k:
        print(minSize)
        return
    i = 0
    total = n - 1
    while 2 * k > n:
        (n, k) = (n - 1, k - 1)
    for i in range(k):
        minSize = max(minSize, s[i] + s[n - i - 1])
    print(minSize)


def __starting_point():
    main()


__starting_point()
