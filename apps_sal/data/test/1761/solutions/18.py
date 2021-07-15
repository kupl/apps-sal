def main():
    from sys import stdin
    l = stdin.read().splitlines()
    sms = iter(l[-1])
    l[0] = l[-1] = ''
    good = set("abcdefghijklmnopqrstuvwxyz0123456789<>")
    try:
        for a in "<3".join(l):
            b = next(sms)
            while b != a:
                b = next(sms)
                if b not in good:
                    print('no')
                    return
    except StopIteration:
        print('no')
    else:
        try:
            while True:
                b = next(sms)
                if b not in good:
                    print('no')
                    return
        except StopIteration:
            print('yes')


def __starting_point():
    main()

__starting_point()
