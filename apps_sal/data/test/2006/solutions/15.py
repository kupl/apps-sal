def main():
    n, _ = list(map(int, input().split()))
    res = set()
    for _ in range(n):
        a = input()
        s, g = a.find("S"), a.find("G")
        if s < g:
            print(-1)
            return
        res.add(s - g)
    print(len(res))


def __starting_point():
    main()


__starting_point()
