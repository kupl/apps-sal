def print_chessboard(size: int) -> None:
    n_coders = size * size // 2
    line = ['C.' * (size // 2), '.C' * (size // 2)]

    if size % 2 != 0:
        n_coders += 1
        line[0] += 'C'
        line[1] += '.'

    print(n_coders)

    for i in range(size):
        print(line[i % 2])

    return


def main() -> int:
    n = int(input())
    print_chessboard(n)

    return 0


def __starting_point():
    main()
__starting_point()
