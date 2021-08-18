import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def in_n(): return int(readline())
def in_nn(): return list(map(int, readline().split()))
def in_s(): return readline().rstrip().decode('utf-8')
def in_nl(): return list(map(int, readline().split()))
def in_nl2(H): return [in_nl() for _ in range(H)]
def in_map(): return [s == ord('.') for s in readline() if s != ord('\n')]
def in_map2(H): return [in_map() for _ in range(H)]
def in_all(): return list(map(int, read().split()))


def main():

    A, B = in_nn()

    grid = [[''] * 100 for _ in range(100)]
    for y in range(100):
        for x in range(100):
            if 0 <= y < 50:
                grid[y][x] = '
            else:
                grid[y][x] = '.'

    for y in range(49):
        for x in range(100):
            if y % 2 == 0 and x % 2 == 0:
                if A > 1:
                    grid[y][x] = '.'
                    A -= 1

    for y in range(51, 100):
        for x in range(100):
            if y % 2 == 1 and x % 2 == 0:
                if B > 1:
                    grid[y][x] = '
                    B -= 1

    print((100, 100))
    for y in range(100):
        print((''.join(grid[y])))


def __starting_point():
    main()


__starting_point()
