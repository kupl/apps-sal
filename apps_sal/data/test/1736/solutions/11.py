def main():
    n, t = map(int, input().split())
    l = list(map(int, input().split()))
    start, res = 0, []
    for stop, a in enumerate(l):
        t -= a
        while t < 0:
            t += l[start]
            start += 1
        res.append(stop - start)
    print(max(res) + 1)


def __starting_point():
    main()


__starting_point()
