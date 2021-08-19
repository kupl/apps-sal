import sys
input = sys.stdin.readline


def s(n):
    return sum(map(int, list(str(n))))


def f(x):
    nines = max(0, len(str(x)) - 3)
    base = 10 ** nines - 1
    d = 10 ** nines
    snuke = x
    ratio = x / s(x)
    candidate = base + (x - base + d - 1) // d * d
    for _ in range(150):
        new_ratio = candidate / s(candidate)
        if new_ratio < ratio:
            snuke = candidate
            ratio = new_ratio
        candidate += d
    return snuke


def main():
    k = int(input())
    snuke = 0
    for _ in range(k):
        snuke = f(snuke + 1)
        print(snuke)


def __starting_point():
    main()


__starting_point()
