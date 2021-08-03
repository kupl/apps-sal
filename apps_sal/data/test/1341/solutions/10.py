__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    (s, t) = input(), input()
    i = 0

    for instruction in t:
        if instruction == s[i]:
            i += 1

    print(i + 1)
    return 0


def __starting_point():
    exit(main())


__starting_point()
