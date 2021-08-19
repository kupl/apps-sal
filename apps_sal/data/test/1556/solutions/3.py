def main():
    from heapq import heapify, heappop, heappushpop, heappush
    (n, k, x) = map(int, input().split())
    (l, sign, h) = (list(map(int, input().split())), [False] * n, [])

    def helper():
        return print(' '.join((str(-a if s else a) for (a, s) in zip(l, sign))))
    for (i, a) in enumerate(l):
        if a < 0:
            sign[i] = True
            h.append((-a, i))
        else:
            h.append((a, i))
    heapify(h)
    (a, i) = heappop(h)
    if 1 - sum(sign) % 2:
        j = min(a // x + (1 if a % x else 0), k)
        a -= j * x
        if a > 0:
            l[i] = a
            return helper()
        k -= j
        a = -a
        sign[i] ^= True
    for _ in range(k):
        (a, i) = heappushpop(h, (a, i))
        a += x
    l[i] = a
    for (a, i) in h:
        l[i] = a
    helper()


def __starting_point():
    main()


__starting_point()
