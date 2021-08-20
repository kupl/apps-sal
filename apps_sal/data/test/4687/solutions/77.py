def main():
    (n, k) = list(map(int, input().split()))
    arr = sorted([list(map(int, input().split())) for i in range(n)])
    for ab in arr:
        k -= ab[1]
        if k <= 0:
            ans = ab[0]
            break
    print(ans)


def __starting_point():
    main()


__starting_point()
