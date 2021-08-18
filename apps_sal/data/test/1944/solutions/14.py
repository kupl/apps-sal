

def is_sorted(l, f):
    return all(f(a, b) for a, b in zip(l[:-1], l[1:]))


def main():
    n = int(input())

    lst = map(lambda _: input(), range(n))
    lst = map(lambda s: tuple(map(int, s.split())), lst)
    lst = sorted(lst)

    if is_sorted(lst, lambda a, b: a[1] <= b[1]):
        print("Poor Alex")
    else:
        print("Happy Alex")


def __starting_point():
    main()


__starting_point()
