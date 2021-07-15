def main():
    _, dd, res = input(), {}, 0
    he = list(zip(list(map(int, input().split())), list(map(int, input().split()))))
    for h, e in he:
        le, x = dd.get(h, (-1, 0))
        dd[h] = (le + 1, x + e)
    he.sort(key=lambda _: _[1], reverse=True)
    for h, (le, x) in list(dd.items()):
        if le:
            for h1, e in he:
                if h1 < h:
                    x += e
                    le -= 1
                    if not le:
                        break
        if res < x:
            res = x
    print(sum(e for h, e in he) - res)


def __starting_point():
    main()

__starting_point()
