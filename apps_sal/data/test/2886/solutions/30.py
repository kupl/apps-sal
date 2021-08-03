import re


def get_char_list():
    return [chr(ord('a') + i) for i in range(26)]


def main():
    S = input()
    N = len(S)
    char_list = get_char_list()
    for c in char_list:
        for pattern in ['{}.{}'.format(c, c), '{}{}'.format(c, c)]:
            m = re.search(pattern, S)
            if m is not None:
                sp = m.span()
                print('{} {}'.format(sp[0] + 1, sp[1]))
                return
    print('{} {}'.format(-1, -1))


def __starting_point():
    main()


__starting_point()
