wd = 'SUN MON TUE WED THU FRI SAT'.split()
wd = list(reversed(wd))


def solve(S: str):
    idx = wd.index(S)
    return idx + 1


def main():
    S = input().strip()
    answer = solve(S)
    print(answer)


def __starting_point():
    main()


__starting_point()
