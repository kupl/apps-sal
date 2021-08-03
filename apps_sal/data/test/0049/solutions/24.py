def get_kth_digit(i):
    if i < 10:
        return i

    batch = 9
    count = 9
    width = 1

    while i > 10 * batch * (width + 1) + count:
        batch *= 10
        width += 1
        count += batch * width

    k = i - count - 1
    num = 10 ** width + k // (width + 1)
    return str(num)[k % (width + 1)]


def main():
    i = int(input())

    print(get_kth_digit(i))


def __starting_point():
    main()


__starting_point()
