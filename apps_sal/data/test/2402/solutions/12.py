def main():
    import sys
    input = sys.stdin.readline

    for _ in range(int(input())):
        N, x, y = list(map(int, input().split()))

        worst = min(x + y - 1, N)
        if x + y + 1 - N <= 1:
            best = 1
        else:
            best = min(x + y + 1 - N, N)
        print(best, worst)


def __starting_point():
    main()


__starting_point()
