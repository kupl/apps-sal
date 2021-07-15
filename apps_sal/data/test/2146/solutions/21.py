def main():
    n = int(input())
    aa = list(map(int, input().split()))
    l, nxt = [n] * (n + 1), [0]
    l[0] = l[n] = 0
    for t in range(1, n):
        cur, nxt = nxt, []
        for v in cur:
            for u in v - 1, v + 1, aa[v] - 1:
                if l[u] > t:
                    l[u] = t
                    nxt.append(u)
        if not nxt:
            break
    del l[n]
    print(' '.join(map(str, l)))


def __starting_point():
    main()

__starting_point()
