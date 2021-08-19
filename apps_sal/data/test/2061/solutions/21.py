def main():

    def dfs(x, y):
        nonlocal inner
        if land[y][x] == '.':
            s = 1
            land[y][x] = '*'
            if x:
                s += dfs(x - 1, y)
            else:
                inner = False
            if x + 1 < m:
                s += dfs(x + 1, y)
            else:
                inner = False
            if y:
                s += dfs(x, y - 1)
            else:
                inner = False
            if y + 1 < n:
                s += dfs(x, y + 1)
            else:
                inner = False
            return s
        return 0
    (n, m, k) = list(map(int, input().split()))
    land = [list(input()) for _ in range(n)]
    sav = [row[:] for row in land]
    lakes = []
    for (y, row) in enumerate(land):
        for (x, f) in enumerate(row):
            inner = True
            s = dfs(x, y)
            if s and inner:
                lakes.append((s, x, y))
    (land, res) = (sav, 0)
    for (_, x, y) in sorted(lakes)[:len(lakes) - k]:
        res += dfs(x, y)
    print(res)
    for row in land:
        print(''.join(row))


def __starting_point():
    from sys import setrecursionlimit
    setrecursionlimit(3000)
    main()


__starting_point()
