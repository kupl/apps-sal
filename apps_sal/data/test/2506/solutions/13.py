# python3
from bisect import bisect_left
INF = int(1e9)


def main():
    n, m = list(map(int, input().split()))
    a = [int(i) for i in input().split()]
    a.sort()
    ac = [0]
    for i in range(n):
        ac.append(ac[i] + a[i])

    def chk(x):
        cnt = 0
        for i in range(n):
            pos = bisect_left(a, x - a[i])
            cnt += (n - pos)
        return (cnt < m)

    l = 0
    r = INF
    while r - l > 1:
        mid = (l + r) // 2
        if chk(mid):
            r = mid
        else:
            l = mid

    cnt = 0
    sgm = 0
    for i in range(n):
        pos = bisect_left(a, r - a[i])
        cnt += (n - pos)
        sgm += a[i] * (n - pos) + (ac[n] - ac[pos])

    print((sgm + (m - cnt) * l))


main()
