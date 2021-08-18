
import fileinput


def solve(n, m, a, b):
    cost = 0
    if b < (m * a) and m > 0:
        cost = (n // m) * b
        cost += min(b, (n % m) * a)
    else:
        cost = n * a

    return cost


def __starting_point():
    for line in fileinput.input():
        n, m, a, b = list(map(int, line.split(' ')))

        sol = solve(n, m, a, b)
        print(sol)


__starting_point()
