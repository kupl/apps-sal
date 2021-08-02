from bisect import bisect_left


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * (n + 1)
    for i in range(n):
        b[i + 1] = a[i] + b[i]
    ok = 0
    ng = 2 * 10**5 + 5
    while ok + 1 < ng:
        mid = (ok + 1 + ng) // 2
        buf = 0
        for i in range(n):
            p = mid - a[i]
            buf += n - bisect_left(a, p)
        if buf >= m:
            ok = mid
        else:
            ng = mid
    ans = 0
    num = 0
    tot = 0
    for i in range(n):
        p = ok - a[i]
        index = bisect_left(a, p)
        num += n - index
        tot += b[n] - b[index]
        tot += a[i] * (n - index)
    ans = tot - (num - m) * ok
    print(ans)


def __starting_point():
    main()


__starting_point()
