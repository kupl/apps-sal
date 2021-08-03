__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    (n, k) = map(int, input().split())
    times = [int(word) for word in input().split()]
    max = 5 - k

    result = sum(1 for time in times if time <= max)
    print(result // 3)

    return 0


def __starting_point():
    exit(main())


__starting_point()
