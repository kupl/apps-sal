def main():
    a, b, c, res, nxt = -1, -1, 0, [1], [True]
    while b - a < c - b:
        cur, nxt = nxt, [False] * (len(nxt) + 50)
        for p in 1, 5, 10, 50:
            for i, f in enumerate(cur):
                if f:
                    nxt[i + p] = True
        a, b, c = b, c, sum(nxt)
        res.append(c)
    n = int(input())
    print(res[n] if len(res) > n else c + (c - b) * (n - len(res) + 1))


def __starting_point():
    main()

__starting_point()
