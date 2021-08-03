__author__ = "House"

import bisect


def __starting_point():
    n = int(input())
    s = [int(i) for i in input().split()]
    f = [[s[0], 0]]
    outp = list()
    for i in range(1, n):
        now = [s[i], i]
        idx = bisect.bisect_left(f, now)
        ans = 0
        if idx == 0:
            ans = f[0][0]
        elif idx == i:
            ans = f[idx - 1][0]
        else:
            if f[idx][1] < f[idx - 1][1]:
                ans = f[idx - 1][0]
            else:
                ans = f[idx][0]
        f[idx:idx] = [now]
        outp.append(str(ans))
    print(" ".join(outp))


__starting_point()
