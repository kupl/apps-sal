def read_to_list(count):
    s = []
    for i in range(count):
        start, stop = [int(i) for i in input().split()]
        s.extend(list(range(start, stop + 1)))
    return s


def has_equal_items(first, second):
    for item in first:
        if item in second:
            return True
    return False


def update_list(l, t):
    for i in range(len(l)):
        l[i] += t


def main():
    p, q, l, r = [int(i) for i in input().split()]
    z, x = read_to_list(p), read_to_list(q)
    if l > 0:
        update_list(x, l)
    count = 1 if has_equal_items(z, x) else 0
    for t in range(l, r):
        update_list(x, 1)
        if has_equal_items(x, z):
            count += 1
    print(count)


def __starting_point():
    main()


__starting_point()
