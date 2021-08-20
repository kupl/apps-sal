from copy import deepcopy
from fractions import Fraction


def main():
    (n, a, b) = list(map(int, input().split()))
    v = list(map(int, input().split()))
    dp = [[0, 0] for i in range(n + 1)]
    dp[0] = [0, 1]
    for j in range(n):
        dppre = deepcopy(dp)
        for i in range(n):
            vnew = dppre[i][0] + v[j]
            ways = dppre[i][1]
            if vnew > dp[i + 1][0]:
                dp[i + 1] = [vnew, ways]
            elif vnew == dp[i + 1][0]:
                dp[i + 1][1] += ways
    maxave = 0
    for i in range(a, b + 1):
        maxave = max(maxave, Fraction(dp[i][0], i))
    ways = 0
    for i in range(a, b + 1):
        if Fraction(dp[i][0], i) == maxave:
            ways += dp[i][1]
    print(float(maxave))
    print(ways)


def __starting_point():
    main()


__starting_point()
