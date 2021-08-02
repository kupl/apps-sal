import numpy as np


def main():
    def check(m):
        DP = np.full(k + 1, False)
        DP[0] = True
        for i in range(n):
            if i == m:
                continue
            DP[a[i]:] = np.logical_or(DP[a[i]:], DP[:k + 1 - a[i]])
        return any(DP[i] for i in range(k - a[m], k))

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a = [i for i in a if i < k]
    a.sort()
    n = len(a)

    left = -1
    right = n

    while right - left > 1:
        mid = (right + left) // 2
        if check(mid):
            right = mid
        else:
            left = mid

    print(right)


main()
