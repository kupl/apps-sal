from collections import Counter


def __starting_point():
    n, k = list(map(int, input().split()))
    s = input()
    c = Counter(s)
    min_symbols = min(c[chr(ord("A") + i)] for i in range(k))
    print(min_symbols * k)


__starting_point()
