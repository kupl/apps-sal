def main():
    n = int(input())
    l = [input() for _ in range(n)]
    res = []
    for y, s in enumerate(l):
        for x, c in enumerate(s):
            if c == '.':
                res.append((x, y))
                break
    if len(res) < n:
        res = []
        for x in range(n):
            for y in range(n):
                if l[y][x] == '.':
                    res.append((x, y))
                    break
        if len(res) < n:
            print(-1)
            return
    for x, y in res:
        print(y + 1, x + 1)


def __starting_point():
    main()

__starting_point()
