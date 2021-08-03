import numpy as np
import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    n, t = map(int, input().split())
    dp = np.zeros(t, dtype=int)
    food = []
    for _ in range(n):
        a, b = map(int, input().split())
        food.append([a, b])
    food.sort(key=lambda x: x[0] * -1)
    for j in range(n):
        a, b = food[j][0], food[j][1]
        a = min(a, t)
        dptmp = np.zeros(t, dtype=int)
        dptmp[a:] = np.maximum(dp[a:], dp[:-a] + b)
        dptmp[:a] = np.maximum(np.full(a, b, dtype=int), dp[:a])
        dp = dptmp
    print(dp[-1])


def __starting_point():
    main()


__starting_point()
