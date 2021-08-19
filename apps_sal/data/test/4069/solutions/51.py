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
    (X, K, D) = input_to_int_map()
    temp = abs(X) // D
    if K < temp:
        return int(abs(X) - K * D)
    if (K - temp) % 2 == 0:
        return int(abs(X) - D * temp)
    return int(abs(abs(X) - D * temp - D))


def __starting_point():
    print(main())


__starting_point()
