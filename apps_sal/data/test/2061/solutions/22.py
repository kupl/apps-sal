def main():
    def dfs(x, y):
        nonlocal inner
        if d[x, y] == '.':
            d[x, y], s = '*', 1
            for uv in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                try:
                    s += dfs(*uv)
                except KeyError:
                    inner = False
            return s
        return 0

    n, m, k = list(map(int, input().split()))
    d = {(x, y): c for y in range(n) for x, c in enumerate(input())}
    sav, lakes = d.copy(), []
    for y in range(n):
        for x in range(m):
            inner = True
            s = dfs(x, y)
            if s and inner:
                lakes.append((s, x, y))
    d, res = sav, 0
    for _, x, y in sorted(lakes)[:len(lakes) - k]:
        res += dfs(x, y)
    print(res)
    for y in range(n):
        print(''.join(d[x, y] for x in range(m)))


def __starting_point():
    from sys import setrecursionlimit

    setrecursionlimit(6000)
    main()

__starting_point()
