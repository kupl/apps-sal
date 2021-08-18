
import itertools

CHARGE = 1
DISCHARGE = -2


def solve(j1, j2):
    if j1 == 1 and j2 == 1:
        return 0
    last_charged = 1 if j1 >= j2 else 2
    for t in itertools.count():
        if j1 <= 0 or j2 <= 0:
            return t
        elif j1 <= 2:
            j1 += CHARGE
            j2 += DISCHARGE
            last_charged = 1
        elif j2 <= 2:
            j1 += DISCHARGE
            j2 += CHARGE
            last_charged = 2
        elif last_charged == 1:
            j1 += CHARGE
            j2 += DISCHARGE
        elif last_charged == 2:
            j1 += DISCHARGE
            j2 += CHARGE


def main():
    j1, j2 = list(map(int, input().split()))
    print(solve(j1, j2))


def __starting_point():
    main()


__starting_point()
