import sys


def main():
    input = sys.stdin.readline
    inf = 10**8 + 1
    N = int(input())
    const_x_max, right_max, left_max = -inf, -inf, -inf
    const_x_min, right_min, left_min = inf, inf, inf
    const_y_max, up_max, down_max = -inf, -inf, -inf
    const_y_min, up_min, down_min = inf, inf, inf
    for _ in range(N):
        x, y, d = list(map(str, input().strip().split()))
        x, y = int(x), int(y)

        if d == 'R':
            right_max = max(right_max, x)
            right_min = min(right_min, x)
            const_y_max = max(const_y_max, y)
            const_y_min = min(const_y_min, y)
        elif d == 'L':
            left_max = max(left_max, x)
            left_min = min(left_min, x)
            const_y_max = max(const_y_max, y)
            const_y_min = min(const_y_min, y)
        elif d == 'U':
            const_x_max = max(const_x_max, x)
            const_x_min = min(const_x_min, x)
            up_max = max(up_max, y)
            up_min = min(up_min, y)
        else:
            const_x_max = max(const_x_max, x)
            const_x_min = min(const_x_min, x)
            down_max = max(down_max, y)
            down_min = min(down_min, y)

    inflections = set([0])
    # The time when the slope of max_x changes.
    # 1. from decrease to constant.
    inflections.add(max(0, left_max - const_x_max))
    # 2. from decrease to increase.
    inflections.add(max(0, (left_max - right_max) / 2))
    # 3. from constant to increase.
    inflections.add(max(0, const_x_max - right_max))

    # The time when the slope of min_x changes.
    # 4. from increase to constatnt.
    inflections.add(max(0, const_x_min - right_min))
    # 5. from increase to decrease.
    inflections.add(max(0, (left_min - right_min) / 2))
    # 6. from constant to decrease.
    inflections.add(max(0, left_min - const_x_min))

    # The time when the slope of max_y changes.
    # 7. from decrease to constant.
    inflections.add(max(0, down_max - const_y_max))
    # 8. from decrease to increase.
    inflections.add(max(0, (down_max - up_max) / 2))
    # 9. from constant to increase.
    inflections.add(max(0, const_y_max - up_max))

    # The time when the slope of min_y changes.
    # 10. from increase to constatnt.
    inflections.add(max(0, const_y_min - up_min))
    # 11. from increase to decrease.
    inflections.add(max(0, (down_min - up_min) / 2))
    # 12. from constant to decrease.
    inflections.add(max(0, down_min - const_y_min))

    def get_val(t):
        x0 = max(const_x_max, right_max + t, left_max - t)
        x1 = min(const_x_min, right_min + t, left_min - t)
        y0 = max(const_y_max, up_max + t, down_max - t)
        y1 = min(const_y_min, up_min + t, down_min - t)

        return (x0 - x1) * (y0 - y1)

    ans = 10**18
    for t in inflections:
        ans = min(ans, get_val(t))

    return ans


def __starting_point():
    print((main()))


__starting_point()
