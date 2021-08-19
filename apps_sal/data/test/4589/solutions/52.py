import typing
from typing import List, Counter
from itertools import product


class Grid:
    def __init__(self, field: List[str]):
        self.setField(field)

    def setField(self, field) -> None:
        self.column: int = len(field)
        self.row: int = len(field[0])
        self.field: List[List[str]] = [list(line) for line in field]

    def searchBomb(self) -> None:
        for i, j in product(range(self.column), range(self.row)):
            conn = tuple((i - 1 + k // 3, j - 1 + k % 3) for k in range(9))
            conn = tuple((x, y) for x, y in conn if 0 <= x < self.column and 0 <= y < self.row)
            if self.field[i][j] == '.':
                self.field[i][j] = str(Counter(self.field[x][y] for x, y in conn)['#'])

    def print(self) -> None:
        for line in self.field:
            print(''.join(line))


def main():
    with open(0) as f:
        H, W = map(int, f.readline().split())
        S = [line.strip() for line in f.readlines()]
    grid = Grid(S)
    grid.searchBomb()
    grid.print()


def __starting_point():
    main()


__starting_point()
