
import sys
input = sys.stdin.readline


def main():
    n, m = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())))
    import bisect
    l, r = 0, a[-1] * 2 + 1
    while r - l > 1:
        x = (l + r) // 2
        cnt = 0
        for ai in a:
            cnt += n - bisect.bisect_left(a, x - ai)
        if cnt >= m:
            l = x
        else:
            r = x
    x = (l + r) // 2
    ans = 0
    cnt = 0
    a_ = 0
    cs_a = [0]
    for ai in a:
        a_ += ai
        cs_a.append(a_)
    for ai in a:
        bi = bisect.bisect_right(a, x - ai)
        cnt += n - bi
        ans += cs_a[-1] - cs_a[bi] + (n - bi) * ai
    print((ans + (m - cnt) * x))


def __starting_point():
    main()


__starting_point()
