def main():
    from heapq import heappop, heappush
    from sys import stdin
    _, *l = stdin.read().splitlines()
    h, res = [], []
    for s in l:
        if s == ("removeMin"):
            if h:
                heappop(h)
            else:
                res.append("insert 1")
        else:
            c, x = s.split()
            x = int(x)
            if c == "insert":
                heappush(h, x)
            else:
                while h and h[0] < x:
                    heappop(h)
                    res.append("removeMin")
                if not h or h[0] > x:
                    heappush(h, x)
                    res.append("insert %d" % x)
        res.append(s)
    print(len(res))
    print('\n'.join(res))


def __starting_point():
    main()


__starting_point()
