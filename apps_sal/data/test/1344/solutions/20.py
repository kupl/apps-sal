
import sys


def main():
    n, = stdin_get_ints_from_line()
    arr = stdin_get_ints_list_from_line()

    results = []
    result = 1

    if n == 1:
        return result

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            result += 1
        else:
            results.append(result)
            result = 1

    results.append(result)

    return max(results)


def stdin_get_ints_from_line():
    return (int(x) for x in sys.stdin.readline().strip().split(' '))


def stdin_get_ints_list_from_line():
    return list(int(x) for x in sys.stdin.readline().strip().split(' '))


def stdin_get_string_from_line():
    return sys.stdin.readline().strip()


def __starting_point():
    print(main())


__starting_point()
