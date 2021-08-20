def main():
    from heapq import heappush, heappushpop
    n = int(input())
    (*a,) = list(map(int, input().split()))
    to_rm = [0] * (n * 3)
    h = []
    for x in a[:n]:
        heappush(h, x)
    mid = tuple(enumerate(a[n:n * 2], n))
    t = 0
    for (i, x) in mid:
        mi = heappushpop(h, x)
        t += mi
        to_rm[i] = -t
    h = []
    for x in a[n * 2:n * 3]:
        heappush(h, -x)
    t = 0
    for (i, x) in reversed(mid):
        ma = -heappushpop(h, -x)
        t += ma
        to_rm[i - 1] += t
    tot = sum(a)
    ret = -10 ** 30
    s = sum(a[:n - 1])
    for tail in range(n - 1, n * 2):
        s += a[tail]
        ret = max(ret, s - (tot - s) + to_rm[tail])
    print(ret)


def __starting_point():
    main()


__starting_point()
