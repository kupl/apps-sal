from typing import List


def answer(w: int, h: int, n: int, xyas: List[List[int]]) -> int:
    bottom_left_corner_of_white = {'x': 0, 'y': 0}
    top_right_corner_of_white = {'x': w, 'y': h}

    for xya in xyas:
        x, y, a = xya
        if a == 1:
            if bottom_left_corner_of_white['x'] < x:
                bottom_left_corner_of_white['x'] = x
        if a == 2:
            if x < top_right_corner_of_white['x']:
                top_right_corner_of_white['x'] = x
        if a == 3:
            if bottom_left_corner_of_white['y'] < y:
                bottom_left_corner_of_white['y'] = y
        if a == 4:
            if y < top_right_corner_of_white['y']:
                top_right_corner_of_white['y'] = y

    width_of_white = max(0, top_right_corner_of_white['x'] - bottom_left_corner_of_white['x'])
    height_of_white = max(0, top_right_corner_of_white['y'] - bottom_left_corner_of_white['y'])

    return width_of_white * height_of_white


def main():
    w, h, n = map(int, input().split())
    xyas = [list(map(int, input().split())) for _ in range(n)]
    print(answer(w, h, n, xyas))


def __starting_point():
    main()
__starting_point()
