def main():
    from sys import stdin
    l = stdin.read().splitlines()
    sms = iter(l[-1])
    l[0] = l[-1] = ''
    try:
        for c in "<3".join(l):
            while next(sms) != c:
                pass
    except StopIteration:
        print('no')
    else:
        print('yes')


def __starting_point():
    main()

__starting_point()
