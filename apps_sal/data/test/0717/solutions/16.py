def solve():
    N = int(input())
    a, b = map(int, input().split())
    day = a
    for a, b in ((map(int, input().split())) for _ in [0] * (N - 1)):
        if day < a:
            day = a
        else:
            diff = b - ((day - a) % b)
            day = day + diff if diff > 0 else day + b

    print(day)


def __starting_point():
    solve()


__starting_point()
