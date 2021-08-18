from math import *


def __starting_point():
    k, d, t = map(int, input().split())

    per = ceil(k / d) * d
    fire = k if d >= k else per - per % k
    warm = (per - fire) / 2

    ans = t // (fire + warm) * per

    remain = t - t // (fire + warm) * (fire + warm)

    if remain <= fire:
        ans += remain
    else:
        ans += fire
        remain -= fire
        ans += remain * 2
    print(ans)


__starting_point()
