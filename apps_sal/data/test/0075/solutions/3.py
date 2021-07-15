#!/usr/bin/env pypy3

import array
import itertools

IMPOSSIBLE = (-1, -1)


def place_bomb(height, width, is_wall):
    # zero-based
    walls_row = array.array("L", (sum(row) for row in is_wall))
    walls_column = array.array("L")
    for column_idx in range(width):
        walls_column.append(sum(is_wall[r][column_idx] for r in range(height)))
    total_walls = sum(walls_row)
    for bomb_r, bomb_c in itertools.product(list(range(height)), list(range(width))):
        wiped_walls = walls_row[bomb_r] + walls_column[bomb_c]
        wiped_walls -= is_wall[bomb_r][bomb_c]
        if wiped_walls == total_walls:
            # one-based
            return (bomb_r + 1, bomb_c + 1)
    else:
        return IMPOSSIBLE


def main():
    height, width = list(map(int, input().split()))
    is_wall = [array.array("B",
               [c == "*" for c in input()]) for _ in range(height)]
    ans = place_bomb(height, width, is_wall)
    if ans != IMPOSSIBLE:
        print("YES")
        print(*ans)
    else:
        print("NO")


def __starting_point():
    main()

__starting_point()
