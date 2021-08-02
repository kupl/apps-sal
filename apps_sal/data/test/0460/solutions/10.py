import sys

input_ = sys.stdin.readline


def precompute_places():
    res = {}

    for i in range(476):
        res[i] = get_tshirt_winners(i)

    return res


def get_tshirt_winners(i):
    winners = set()

    for _ in range(25):
        i = (i * 96 + 42) % 475
        winners.add(i + 26)

    return winners


def can_haz_tshirt(s, p, places):
    i = (s // 50) % 475

    if p in places[i]:
        return True
    return False


def main():
    p, x, y = list(map(int, input_().split()))

    places = precompute_places()

    x_down = x
    while x_down >= y:
        if can_haz_tshirt(x_down, p, places):
            return 0
        x_down -= 50

    x += 100
    successes = 1
    for _ in range(476):
        if can_haz_tshirt(x, p, places) or can_haz_tshirt(x - 50, p, places):
            return successes

        x += 100
        successes += 1

    return -1


def __starting_point():
    print(main())


__starting_point()
