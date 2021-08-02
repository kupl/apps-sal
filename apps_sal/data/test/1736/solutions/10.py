def main():
    n, t = map(int, input().split())
    l = list(map(int, input().split()))
    start = stop = 0
    res = []
    try:
        while True:
            while t >= 0:
                res.append(stop - start)
                if stop == n:
                    raise StopIteration
                t -= l[stop]
                stop += 1
            while t < 0:
                t += l[start]
                start += 1
    except StopIteration:
        print(max(res))


def __starting_point():
    main()


__starting_point()
