def main():
    N = int(input())
    UV = [tuple(map(int, input().split())) for _ in range(N - 1)]
    ans = 0
    for i in range(1, N + 1):
        ans += i * (N - i + 1)
    for u, v in UV:
        if u > v:
            u, v = v, u
        ans -= u * (N - v + 1)
    print(ans)


def __starting_point():
    main()


__starting_point()
