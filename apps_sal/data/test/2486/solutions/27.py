import numpy as np


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) >= k:
        a.sort()
        L, R = -1, n - 1
        while L + 1 < R:
            P = (L + R + 1) // 2
            if k <= a[P]:
                R = P
                continue
            dp = np.zeros((k + 1), dtype=np.bool)
            dp[0] = True
            for j in range(n):
                if k <= a[j] or j == P:
                    continue
                dp[a[j]:] |= dp[:-a[j]]
            f = False
            for j in range(k - a[P], k):
                f |= dp[j]
            if f:
                R = P
            else:
                L = P
        print(R)
    else:
        print(n)


def __starting_point():
    main()


__starting_point()
