import sys

sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inl(): return [int(x) for x in sys.stdin.readline().split()]
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    h, w = inl()
    grid = [None] * h
    for i in range(h):
        grid[i] = ins()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != "#":
                continue
            ok = False
            for k in range(4):
                i2 = i + dy[k]
                j2 = j + dx[k]
                if 0 <= i2 < h and 0 <= j2 < w and grid[i2][j2] == "#":
                    ok = True
                    break
            if not ok:
                return False
    return True


print("Yes" if solve() else "No")
