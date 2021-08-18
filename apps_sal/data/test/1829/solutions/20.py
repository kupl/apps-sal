

def solve():
    n, m = list(map(int, input().split()))

    words_n = set(input() for _ in range(n))
    words_m = set(input() for _ in range(m))

    only_m = len(words_m - words_n)
    only_n = len(words_n - words_m)
    both = len(words_m) - only_m

    if both % 2 == 1:
        only_n += 1
    return only_n > only_m


def __starting_point():
    print("YES" if solve() else "NO")


__starting_point()
