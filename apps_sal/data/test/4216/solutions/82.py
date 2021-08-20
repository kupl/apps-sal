import sys
import pprint as pp


def II():
    return int(sys.stdin.readline())


def MI():
    return list(map(int, sys.stdin.readline().split()))


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


MAXSIZE = (1 << 31) - 1
MINSIZE = -(1 << 31) + 1


def solver(input_int):
    result = len(str(input_int))
    for j in range(1, int(input_int ** 0.5) + 1, +1):
        divide_check = input_int % j != 0
        if divide_check:
            continue
        divide_value = input_int // j
        long_check = len(str(divide_value)) <= result
        if long_check:
            result = len(str(divide_value))
    return result


def __starting_point():
    N = II()
    print('{}'.format(solver(N)))


__starting_point()
