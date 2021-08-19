__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = 'sonhuytran@gmail.com'
__doc__ = ''
__version__ = '1.0'


def has_not_more_than_k_lucky(number: str, k: int) -> bool:
    return number.count('4') + number.count('7') <= k


def count_lucky(numbers: list, k: int) -> int:
    return sum((has_not_more_than_k_lucky(number, k) for number in numbers))


def main() -> int:
    (n, k) = map(int, input().split())
    numbers = input().split()
    print(count_lucky(numbers, k))
    return 0


def __starting_point():
    exit(main())


__starting_point()
