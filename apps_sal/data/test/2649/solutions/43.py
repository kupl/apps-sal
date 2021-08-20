def get_points_and_convert(pts):
    (x, y) = pts
    return (x + y, x - y)


def main():
    n = int(input())
    points = [get_points_and_convert(list(map(int, input().split()))) for _ in range(n)]
    (plus_coords, minus_coords) = list(zip(*points))
    plus_dist = max(plus_coords) - min(plus_coords)
    minus_dist = max(minus_coords) - min(minus_coords)
    print(max(plus_dist, minus_dist))


def __starting_point():
    main()


__starting_point()
