def main():

    def solve(n):
        if n == 1:
            return 1
        return solve(n // 2) * 2 + 1
    H = int(input())
    print(solve(H))


def __starting_point():
    main()


__starting_point()
