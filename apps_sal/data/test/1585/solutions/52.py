from collections import Counter


def lmi():
    return list(map(int, input().split()))


def main():
    (X, Y) = lmi()
    cur = X
    result = 0
    while cur <= Y:
        result += 1
        cur *= 2
    print(result)


def __starting_point():
    main()


__starting_point()
