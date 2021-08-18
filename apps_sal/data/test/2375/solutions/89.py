
def main():
    X, Y = list(map(int, input().split()))

    def solve(x, y):
        """手番が勝つか"""
        return not ((X + Y <= 1) or (abs(X - Y) <= 1))

    cond = solve(X, Y)
    print(('Alice' if cond else 'Brown'))


def __starting_point():
    main()


__starting_point()
