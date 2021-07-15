def main():
    l = list(input())
    a = l[-1]
    l.append('8')
    mask = {'9': ('0', '2', '4', '6', '8'),
            '7': ('0', '2', '4', '6'),
            '5': ('0', '2', '4'),
            '3': ('0', '2',),
            '1': ('0')}[a]
    for i, b in enumerate(l):
        if b in mask:
            if i < len(l) - 1:
                del l[-1]
                l[i], l[-1] = a, b
                print(''.join(l))
                return
    for i in range(len(l) - 2, -2, -1):
        b = l[i]
        if b in ('0', '2', '4', '6', '8'):
            if i != -1:
                del l[-1]
                l[i], l[-1] = a, b
                print(''.join(l))
                return
    print(-1)


def __starting_point():
    main()

__starting_point()
