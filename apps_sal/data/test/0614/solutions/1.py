import sys
from itertools import accumulate


def solve():
    n, m = map(int, input().split())
    w = [[] for i in range(3)]

    for i in range(n):
        wi, ci = map(int, sys.stdin.readline().split())
        wi -= 1
        w[wi].append(ci)

    for i in range(3):
        w[i].sort(reverse=True)

    dp = [0] * (m + 1)
    used = [[0] * 2 for i in range(m + 1)]

    s0 = len(w[0])
    s1 = len(w[1])

    if s0 > 0:
        dp[1] = w[0][0]
        used[1] = [1, 0]

    for i in range(2, m + 1):
        if used[i - 1][0] < s0:
            dp[i] = dp[i - 1] + w[0][used[i - 1][0]]
            used[i] = used[i - 1][:]
            used[i][0] += 1
        else:
            dp[i] = dp[i - 1]
            used[i] = used[i - 1][:]

        if used[i - 2][1] < s1 and dp[i] < dp[i - 2] + w[1][used[i - 2][1]]:
            dp[i] = dp[i - 2] + w[1][used[i - 2][1]]
            used[i] = used[i - 2][:]
            used[i][1] += 1

    pf = [0] + list(accumulate(w[2]))

    ans = max(pf[k] + dp[m - 3 * k] for k in range(min(len(pf), m // 3 + 1)))

    print(ans)


def __starting_point():
    solve()


__starting_point()
