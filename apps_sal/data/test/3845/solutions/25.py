def main():
    A, B = (int(i) for i in input().split())
    grid = [["#" if i < 50 else "."]*100 for i in range(100)]

    for h in range(49):
        if h % 2 == 1:
            continue
        for w in range(0, 100, 2):
            if A > 1:
                grid[h][w] = "."
                A -= 1
            else:
                break
    for h in range(51, 100):
        if h % 2 == 0:
            continue
        for w in range(0, 100, 2):
            if B > 1:
                grid[h][w] = "#"
                B -= 1
            else:
                break
    print((100, 100))
    for r in grid:
        print(("".join(r)))


def __starting_point():
    main()

__starting_point()
