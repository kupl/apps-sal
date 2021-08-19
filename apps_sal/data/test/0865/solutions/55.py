import numpy as np


def __starting_point():
    (N, T) = list(map(int, input().split()))
    menu = list()
    for i in range(N):
        menu_i = tuple(map(int, input().split()))
        menu.append(menu_i)
    menu.sort()
    dp = np.zeros(T, int)
    ans = 0
    for ab in menu:
        ans = max(ans, dp[-1] + ab[1])
        dp[ab[0]:] = np.maximum(dp[ab[0]:], dp[:-ab[0]] + ab[1])
    print(ans)


__starting_point()
