def shift(s, k):
    k %= len(s)
    return s[-k:] + s[:-k]


def process(s, l, r, k):
    return s[:l - 1] + shift(s[l - 1:r], k) + s[r:]


def __starting_point():
    s = input().strip()
    m = int(input())
    for _ in range(m):
        (l, r, k) = [int(x) for x in input().strip().split()]
        s = process(s, l, r, k)
    print(s)


__starting_point()
