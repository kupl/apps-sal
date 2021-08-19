__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = 'sonhuytran@gmail.com'
__doc__ = ''
__version__ = '1.0'


def can_paint(wall: list) -> bool:
    for i in range(3):
        for j in range(3):
            temp = wall[i][j] + wall[i + 1][j] + wall[i][j + 1] + wall[i + 1][j + 1]
            if temp.count('.') != temp.count('#'):
                return True
    return False


def main() -> int:
    wall = [input(), input(), input(), input()]
    print('YES' if can_paint(wall) else 'NO')
    return 0


def __starting_point():
    exit(main())


__starting_point()
