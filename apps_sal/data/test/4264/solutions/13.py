import array
import bisect


def answer(n: int) -> int:
    numbers = array.array('L')

    i = 0
    while 100 ** i <= n:
        start = 100 ** i
        stop = int('9' * len(str(start))) + 1
        numbers.extend(list(range(start, stop)))
        i += 1

    return bisect.bisect_right(numbers, n)


def main():
    n = int(input())
    print((answer(n)))


def __starting_point():
    main()


__starting_point()
