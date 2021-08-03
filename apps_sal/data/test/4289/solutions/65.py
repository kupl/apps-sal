def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n = int(input())
    t, a = Input()
    h = Input()

    h = [t - i * 0.006 for i in h]
    h = [abs(a - i) for i in h]
    min_h = min(h)

    print(h.index(min_h) + 1)


main()
