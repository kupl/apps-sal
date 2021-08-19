def solve():
    (num_pixels, max_group_size) = (int(x) for x in input().split())
    pixels = [int(x) for x in input().split()]
    groups = [None for _ in range(256)]
    for pixel in pixels:
        if groups[pixel] is None:
            smallest_of_group = pixel
            while smallest_of_group >= 0 and smallest_of_group > pixel - max_group_size and (groups[smallest_of_group] is None):
                smallest_of_group -= 1
            if smallest_of_group >= 0 and groups[smallest_of_group] is not None and (pixel - groups[smallest_of_group] + 1 <= max_group_size):
                group_color = groups[smallest_of_group]
            else:
                group_color = smallest_of_group + 1
            smallest_of_group += 1
            for color in range(smallest_of_group, pixel + 1):
                groups[color] = group_color
    print(*(groups[pixel] for pixel in pixels))


solve()
