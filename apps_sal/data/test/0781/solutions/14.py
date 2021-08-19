__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = 'sonhuytran@gmail.com'
__doc__ = ''
__version__ = '1.0'


def is_proper_chessboard(chessboard: list) -> bool:
    propers = ['WBWBWBWB', 'BWBWBWBW']
    for row in chessboard:
        if row != propers[0] and row != propers[1]:
            return False
    return True


def main() -> int:
    chessboard = []
    for _ in range(8):
        chessboard.append(input())
    print('YES' if is_proper_chessboard(chessboard) else 'NO')
    return 0


def __starting_point():
    exit(main())


__starting_point()
