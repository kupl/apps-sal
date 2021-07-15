from itertools import chain


def main():
    input()
    lb, la = [], []
    a = b = -1
    it = iter(sorted(map(int, input().split())))
    try:
        while True:
            c = next(it)
            if a != c:
                a = c
                la.append(a)
            c = next(it)
            if b != c:
                b = c
                lb.append(b)
            pass
    except StopIteration:
        if a == b:
            del lb[-1]
    print(len(la) + len(lb))
    print(' '.join(map(str, chain(la, lb[::-1]))))


def __starting_point():
    main()
__starting_point()
