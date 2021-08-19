def main():
    (n, k) = list(map(int, input().split()))
    ans = 0
    for b in range(1, n + 1):
        (q, r) = divmod(n, b)
        ans += q * max(0, b - k)
        ans += max(0, r - k + 1)
    if k == 0:
        ans -= n
    print(ans)


def __starting_point():
    main()


__starting_point()
