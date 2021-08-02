def main():
    from itertools import permutations

    N, C = list(map(int, input().split()))
    change_cost = [[int(x) for x in input().split()] for _ in range(C)]
    init_color = [[int(x) - 1 for x in input().split()] for _ in range(N)]

    ctr = [[0] * C for _ in range(3)]
    for r in range(N):
        for c in range(N):
            p = (r + c) % 3
            color = init_color[r][c]
            ctr[p][color] += 1

    mi = 1000 * 500 * 500 + 1
    for perm in permutations(list(range(C)), r=3):
        it = iter(perm)
        t = 0
        for p in range(3):
            color_to_be = next(it)
            for color, count in enumerate(ctr[p]):
                t += change_cost[color][color_to_be] * count
        mi = min(mi, t)
    print(mi)


def __starting_point():
    main()


__starting_point()
