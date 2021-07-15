from collections import defaultdict


def main():
    height, width, target_count = [int(x) for x in input().split()]
    count_by_height = defaultdict(int)
    count_by_width = defaultdict(int)
    bomb_locations = set()
    for _ in range(target_count):
        h, w = [int(x) - 1 for x in input().split()]
        count_by_height[h] += 1
        count_by_width[w] += 1
        bomb_locations.add((h, w))
    max_h = max(v for v in list(count_by_height.values()))
    max_w = max(v for v in list(count_by_width.values()))
    max_h_rows = [i for i, x in list(count_by_height.items()) if x == max_h]
    max_w_columns = [i for i, x in list(count_by_width.items()) if x == max_w]
    all_crossing_bomb = all((h, w) in bomb_locations
                            for h in max_h_rows for w in max_w_columns)
    return max_h + max_w - all_crossing_bomb


def __starting_point():
    print((main()))

__starting_point()
