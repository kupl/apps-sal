def solve(H: int, A: int):
    return (H + A - 1) // A


def main():
    (H, A) = list(map(int, input().split()))
    answer = solve(H, A)
    print(answer)


def __starting_point():
    main()


__starting_point()
