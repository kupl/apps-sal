import sys

sys.setrecursionlimit(10 ** 8)
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B = map(int, readline().split())


def solve():
    W = 100
    hw = B // 25 + 2
    hb = A // 25 + 2
    H = hw + hb
    grid = [[i >= hw] * W for i in range(H)]

    def paint_black():
        black = 1
        for r in range(0, hw - 1, 2):
            for c in range(0, W, 2):
                if black == B:
                    return
                grid[r][c] = True
                black += 1

    def paint_white():
        white = 1
        for r in range(hw + 1, H, 2):
            for c in range(0, W, 2):
                if white == A:
                    return
                grid[r][c] = False
                white += 1

    paint_black()
    paint_white()
    return grid


def print_grid(grid):
    h, w = len(grid), len(grid[0])
    print(h, w)
    for r in range(h):
        for c in range(w):
            if grid[r][c]:
                print("
            else:
                print(".", end="")
        print()


def __starting_point():
    print_grid(solve())


__starting_point()
