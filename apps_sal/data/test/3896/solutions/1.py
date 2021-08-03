MODULO = 1000000007


def solve(mask):
    n = len(mask)
    return sum((2 ** k) * (4 ** (n - k - 1)) for k in range(n) if mask[k] == '1') % MODULO


def __starting_point():
    mask = input()
    complexity = solve(mask)
    print(complexity)


__starting_point()
