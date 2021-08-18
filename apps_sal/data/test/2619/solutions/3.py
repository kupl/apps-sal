"""
    Author      : Arif Ahmad
    Date        : 
    Algo        : 
    Difficulty  : 
"""
from sys import stdin, stdout


def main():
    n, q, c = [int(_) for _ in stdin.readline().strip().split()]

    g = [[[0 for i in range(102)] for j in range(102)] for k in range(12)]
    for _ in range(n):
        x, y, s = [int(_) for _ in stdin.readline().strip().split()]
        for t in range(c + 1):
            brightness = (s + t) % (c + 1)
            g[t][x][y] += brightness

    dp = [[[0 for i in range(102)] for j in range(102)] for k in range(12)]
    for t in range(c + 1):
        for x in range(1, 101):
            for y in range(1, 101):
                dp[t][x][y] = dp[t][x - 1][y] + dp[t][x][y - 1] - dp[t][x - 1][y - 1] + g[t][x][y]

    for _ in range(q):
        t, x1, y1, x2, y2 = [int(_) for _ in stdin.readline().strip().split()]
        t = t % (c + 1)
        ans = dp[t][x2][y2] - dp[t][x1 - 1][y2] - dp[t][x2][y1 - 1] + dp[t][x1 - 1][y1 - 1]
        stdout.write(str(ans) + '\n')


def __starting_point():
    main()


__starting_point()
