from sys import stdin, stdout  # only need for big input


def solve():
    h, w = list(map(int, input().split()))
    grid = []
    for _ in range(h):
        s = input()
        assert(len(s) == w)
        grid.append(s)

    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.':
                continue

            isolate = True
            for px in [i - 1, i + 1]:
                if px >= 0 and px < h:
                    if grid[px][j] == '#':
                        isolate = False
            for py in [j - 1, j + 1]:
                if py >= 0 and py < w:
                    if grid[i][py] == '#':
                        isolate = False
            if isolate:
                print("No")
                return

    print("Yes")


def main():
    solve()


def __starting_point():
    main()


__starting_point()
