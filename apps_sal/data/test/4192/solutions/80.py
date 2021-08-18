
YES = 'Yes'
NO = 'No'


def solve(D, T, S):
    return YES if S * T >= D else NO


def main():
    D, T, S = list(map(int, input().split()))
    a = solve(D, T, S)
    print(a)


def __starting_point():
    main()


__starting_point()
