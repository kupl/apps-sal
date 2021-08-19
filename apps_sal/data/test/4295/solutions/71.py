def main():
    (n, k) = list(map(int, input().split()))
    ans = [n % k, abs(n % k - k)]
    return min(ans)


def __starting_point():
    print(main())


__starting_point()
