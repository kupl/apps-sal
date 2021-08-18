from collections import defaultdict


def main():
    H, W, N = list(map(int, input().split(' ')))
    coord_list = [list(map(int, input().split(' '))) for _ in range(N)]
    square_count = defaultdict(int)
    for coord in coord_list:
        coord = tuple(coord)
        if coord[0] + 2 <= H and coord[1] + 2 <= W:
            square_count[coord] += 1
        if coord[0] + 2 <= H and 1 <= coord[1] - 1 and coord[1] + 1 <= W:
            square_count[(coord[0], coord[1] - 1)] += 1
        if coord[0] + 2 <= H and 1 <= coord[1] - 2:
            square_count[(coord[0], coord[1] - 2)] += 1
        if 1 <= coord[0] - 1 and coord[0] + 1 <= H and coord[1] + 2 <= W:
            square_count[(coord[0] - 1, coord[1])] += 1
        if 1 <= coord[0] - 1 and coord[0] + 1 <= H and 1 <= coord[1] - 1 and coord[1] + 1 <= W:
            square_count[(coord[0] - 1, coord[1] - 1)] += 1
        if 1 <= coord[0] - 1 and coord[0] + 1 <= H and 1 <= coord[1] - 2:
            square_count[(coord[0] - 1, coord[1] - 2)] += 1
        if 1 <= coord[0] - 2 and coord[1] + 2 <= W:
            square_count[(coord[0] - 2, coord[1])] += 1
        if 1 <= coord[0] - 2 and 1 <= coord[1] - 1 and coord[1] + 1 <= W:
            square_count[(coord[0] - 2, coord[1] - 1)] += 1
        if 1 <= coord[0] - 2 and 1 <= coord[1] - 2:
            square_count[(coord[0] - 2, coord[1] - 2)] += 1
    count = defaultdict(int)
    for v in list(square_count.values()):
        count[v] += 1
    count_white_only = (H - 2) * (W - 2) - sum(count.values())
    count[0] = count_white_only
    for c in range(0, 10):
        print((count[c]))


def __starting_point():
    main()


__starting_point()
