from itertools import combinations


def main():
    n, l, r, x = [int(t) for t in input().split()]
    c = [int(t) for t in input().split()]

    def is_valid(candidate):
        mx = max(candidate)
        mn = min(candidate)
        sm = sum(candidate)
        return l <= sm <= r and (mx - mn) >= x

    way = 0

    for L in range(2, len(c) + 1):
        for subset in combinations(c, L):
            if is_valid(subset):
                way += 1

    print(way)

def __starting_point():
    main()
__starting_point()
