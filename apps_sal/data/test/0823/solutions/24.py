# python 3
"""
From tutorial: The starting position can be anywhere with a footprint. The footprints can be categorized into 3 types.

only L s
only R s
R s followed by L s

In case 1, we end in the left of all footprints.
In case 2, we end in the right of all footprints.
In case 3, we either end in the rightmost R or the leftmost L

Mine is different from the tutorial, based on intuition, hard to prove its correctness.
"""


def point_on_spiral(x_int, y_int) -> int:
    if x_int == 0 and y_int == 0 or x_int == 1 and y_int == 0:
        return 0
    count = 0
    x_prev, y_prev = 0, 0
    while True:
        spiral, count_mod_4 = divmod(count + 4, 4)
        if count_mod_4 == 0:
            x_curr, y_curr = spiral, -(spiral - 1)
        elif count_mod_4 == 1:
            x_curr, y_curr = spiral, spiral
        elif count_mod_4 == 2:
            x_curr, y_curr = -spiral, spiral
        else:
            x_curr, y_curr = -spiral, -spiral
        dist_to_prev = abs(x_int - x_prev) + abs(y_int - y_prev)
        dist_to_curr = abs(x_int - x_curr) + abs(y_int - y_curr)
        dist_prev_curr = abs(x_curr - x_prev) + abs(y_curr - y_prev)

        if dist_to_curr + dist_to_prev == dist_prev_curr:
            # print(x_prev, y_prev), (x_curr, y_curr), (x_int, y_int)
            return count
        count += 1
        x_prev, y_prev = x_curr, y_curr


def __starting_point():
    """
    Inside of this is the test. 
    Outside is the API
    """
    x, y = list(map(int, input().split()))

    print(point_on_spiral(x, y))


__starting_point()
