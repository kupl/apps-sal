def main():
    A, B = list(map(int, input().split()))
    ans = max(A + B, A - B, A * B)
    print(ans)


def __starting_point():
    main()


__starting_point()
