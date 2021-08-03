def get_next(T):
    [a, b, c] = sorted(T)
    return [b, c, b + c - 1]


def main():
    y, x = [int(s) for s in input().split()]
    T = [x, x, x]
    i = 0
    while max(T) < y:
        T = get_next(T)
        i += 1
    print(2 + i)


main()
