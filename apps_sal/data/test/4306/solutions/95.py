def main():
    A, B, C, D = list(map(int, input().split()))

    ans = max(0, min(B, D) - max(A, C))
    print(ans)


def __starting_point():
    main()

__starting_point()
