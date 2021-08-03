def main3():
    import sys
    sys.setrecursionlimit(100000000)

    N = int(input())
    dp = [-1 for n in range(N + 1)]
    dp[0] = 0
    dp[1] = 1

    def rec(x, dp):
        if x == 1:
            return dp[1]
        elif x == 0:
            return dp[0]
        else:
            l = []
            i = 0
            j = 0
            while 9**(i + 1) <= x:
                i += 1
            while 6**(j + 1) <= x:
                j += 1
            for k in reversed(range(i + 1)):
                tmp = x - 9**k
                if dp[tmp] != -1:
                    l.append(dp[tmp] + 1)
                else:
                    l.append(rec(tmp, dp) + 1)
            for k in reversed(range(j + 1)):
                tmp = x - 6**k
                if dp[tmp] != -1:
                    l.append(dp[tmp] + 1)
                else:
                    l.append(rec(tmp, dp) + 1)
            dp[x] = min(l)
            return dp[x]

    return rec(N, dp)


def __starting_point():
    print(main3())


__starting_point()
