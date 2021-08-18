
FIRST_DIV_START = 1900


def solve():
    n = int(input())
    min_rating = None
    max_rating = None
    for _ in range(n):
        c, d = list(map(int, input().split()))
        if d == 2:
            if max_rating is None:
                max_rating = FIRST_DIV_START - 1
            else:
                max_rating = min(FIRST_DIV_START - 1, max_rating)
            if min_rating is not None and min_rating > max_rating:
                return "Impossible"

            max_rating += c
            if min_rating is not None:
                min_rating += c
        else:
            if min_rating is None:
                min_rating = FIRST_DIV_START
            else:
                min_rating = max(min_rating, FIRST_DIV_START)
            if max_rating is not None and min_rating > max_rating:
                return "Impossible"

            min_rating += c
            if max_rating is not None:
                max_rating += c

    if max_rating is None:
        return "Infinity"
    return max_rating


def __starting_point():
    print(solve())


__starting_point()
