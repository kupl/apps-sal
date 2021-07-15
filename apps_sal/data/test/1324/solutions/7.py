__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'


def main() -> int:
    a = [int(word) for word in input().split()]
    game = input()

    calories = {
        '1': a[0],
        '2': a[1],
        '3': a[2],
        '4': a[3]
    }
    sum_calories = 0

    for brick in game:
        sum_calories += calories[brick]

    print(sum_calories)
    return 0


def __starting_point():
    exit(main())
__starting_point()
