def main():
    (N, M) = list(map(int, input().split()))
    D = [list(map(int, input().split())) for _ in range(N)]
    D.sort()
    ans = 0
    for (a, b) in D:
        if M > b:
            ans += a * b
            M -= b
        else:
            ans += a * M
            break
    print(ans)


def __starting_point():
    main()


__starting_point()
