from itertools import dropwhile, chain


def main():
    zeroes = lambda a: not a
    a, b = [list(chain([0, 0], dropwhile(zeroes, list(map(int, input())))))
            for _ in range(2)]

    def tofib(l):
        i = 0
        while i < len(l) - 1:
            if l[i] > 0 and l[i + 1] > 0:
                l[i] -= 1
                l[i + 1] -= 1
                l[i - 1] += 1
                i -= 3
            i += 1
        return l

    a = list(dropwhile(zeroes, tofib(a)))
    b = list(dropwhile(zeroes, tofib(b)))

    if len(a) < len(b):
        print('<')
        return
    if len(a) > len(b):
        print('>')
        return
    for i in range(len(a)):
        if a[i] < b[i]:
            print('<')
            return
        if a[i] > b[i]:
            print('>')
            return
    print('=')


def __starting_point():
    main()


__starting_point()
