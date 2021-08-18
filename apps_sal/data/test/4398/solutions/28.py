def main():
    _ = int(input())
    S, T = input().split()

    ans = ''
    for s, t in zip(S, T):
        ans += s + t
    print(ans)


def __starting_point():
    main()


__starting_point()
