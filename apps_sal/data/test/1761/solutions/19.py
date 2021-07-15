def main():
    from sys import stdin
    l = stdin.read().splitlines()
    sms = iter(l[-1])
    l[0] = l[-1] = ''
    try:
        for a in "<3".join(l):
            b = next(sms)
            while b != a:
                b = next(sms)
    except StopIteration:
        print('no')
    else:
        print('yes')


def __starting_point():
    main()

__starting_point()
