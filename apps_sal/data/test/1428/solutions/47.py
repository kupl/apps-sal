import itertools


def main():
    N, C = list(map(int, input().split(' ')))
    D = [list(map(int, input().split(' '))) for _ in range(C)]
    grids = [list([int(c) - 1 for c in input().split(' ')]) for _ in range(N)]
    color_counts = [[0 for _ in range(C)] for _ in range(3)]
    for i in range(N):
        for j in range(N):
            g = ((i + 1) + (j + 1)) % 3
            c = grids[i][j]
            color_counts[g][c] += 1
    min_d = 1000 * 500 * 500
    for dest_colors in itertools.permutations(list(range(C)), 3):
        d = 0
        for g in range(3):
            for c in range(C):
                d += color_counts[g][c] * D[c][dest_colors[g]]
        min_d = min([min_d, d])
    print(min_d)


def __starting_point():
    main()


__starting_point()
