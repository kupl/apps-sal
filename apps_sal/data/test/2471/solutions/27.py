from collections import defaultdict


def main():
    H, W, N = list(map(int, input().split(' ')))
    coord_list = [list(map(int, input().split(' '))) for _ in range(N)]
    # count squares (key: coord of top left cell, value: number of appearance)
    square_count = defaultdict(int)
    for coord in coord_list:
        coord = tuple(coord)
        # black cell is located on the top row
        if coord[0] + 2 <= H and coord[1] + 2 <= W:
            square_count[coord] += 1
        if coord[0] + 2 <= H and 1 <= coord[1] - 1 and coord[1] + 1 <= W:
            square_count[(coord[0], coord[1] - 1)] += 1
        if coord[0] + 2 <= H and 1 <= coord[1] - 2:
            square_count[(coord[0], coord[1] - 2)] += 1
        # black cell is located in the middle row
        if 1 <= coord[0] - 1 and coord[0] + 1 <= H and coord[1] + 2 <= W:
            square_count[(coord[0] - 1, coord[1])] += 1
        if 1 <= coord[0] - 1 and coord[0] + 1 <= H and 1 <= coord[1] - 1 and coord[1] + 1 <= W:
            square_count[(coord[0] - 1, coord[1] - 1)] += 1
        if 1 <= coord[0] - 1 and coord[0] + 1 <= H and 1 <= coord[1] - 2:
            square_count[(coord[0] - 1, coord[1] - 2)] += 1
        # black cell is located on the bottom row
        if 1 <= coord[0] - 2 and coord[1] + 2 <= W:
            square_count[(coord[0] - 2, coord[1])] += 1
        if 1 <= coord[0] - 2 and 1 <= coord[1] - 1 and coord[1] + 1 <= W:
            square_count[(coord[0] - 2, coord[1] - 1)] += 1
        if 1 <= coord[0] - 2 and 1 <= coord[1] - 2:
            square_count[(coord[0] - 2, coord[1] - 2)] += 1
    # remove duplicated counts
    count = defaultdict(int)  # key: number of black cells, value: number of squares
    for v in list(square_count.values()):
        count[v] += 1
    count_white_only = (H - 2) * (W - 2) - sum(count.values())
    count[0] = count_white_only
    # print answer
    for c in range(0, 10):
        print((count[c]))


def __starting_point():
    main()


__starting_point()
