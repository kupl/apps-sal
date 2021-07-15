from bisect import bisect_right


def ceil(x, y):
    return (x + y - 1) // y


def main():
    n, d, a = list(map(int, input().split()))
    info = [list(map(int, input().split())) for _ in range(n)]
    info.sort(key=lambda x: x[0])
    x = [x[0] for x in info]
    idx = {}
    for xx in x:
        idx[xx] = bisect_right(x, xx + d * 2)
    delta = [0] * n
    ans = 0
    for i in range(n):
        if i > 0:
            delta[i] += delta[i - 1]
        info[i][1] -= delta[i]
        now = max(ceil(info[i][1], a), 0)
        delta[i] += now * a
        if idx[info[i][0]] < n:
            delta[idx[info[i][0]]] -= now * a
        ans += now
    print(ans)


def __starting_point():
    main()

__starting_point()
