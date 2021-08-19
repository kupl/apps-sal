def solve(string):
    n = int(string)
    return str(sum((i * (n // i) * (n // i + 1) // 2 for i in range(1, n + 1))))


def __starting_point():
    import sys
    print(solve(sys.stdin.read().strip()))


__starting_point()
