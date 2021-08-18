

def input_int():
    return int(input())


def int1(x):
    return int(x) - 1


def input_to_int_map():
    return list(map(int, input().split()))


def input_to_int_tuple():
    return tuple(map(int, input().split()))


def input_to_int_tuple_minus1():
    return tuple(map(int1, input().split()))


def main():
    N = input_int()
    A = input_to_int_tuple()

    result = 0
    max_a = 0
    for a in A:
        if max_a > a:
            result += max_a - a
        max_a = max(a, max_a)

    return result


def __starting_point():
    print((main()))


__starting_point()
