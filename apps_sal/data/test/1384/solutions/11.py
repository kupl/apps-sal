INF = 10 ** 9 + 7


def cutoff(games, pos):
    leave = 0
    for (i, g) in enumerate(games):
        if i < pos:
            if g == 0:
                leave += 1
        elif g == 1:
            leave += 1
    return leave


def main():
    n = int(input())
    games = [int(x) for x in input().split()]
    max_leave = -INF
    for i in range(n + 1):
        max_leave = max(max_leave, cutoff(games, i))
    print(max_leave)


def __starting_point():
    main()


__starting_point()
