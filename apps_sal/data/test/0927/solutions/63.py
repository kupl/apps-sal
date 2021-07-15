#!/usr/bin/env python3

def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))

    # dig: マッチ本数 -> 使える数字
    nm = [999, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    dig = [None for i in range(8)]
    for x in sorted(a):
        dig[nm[x]] = x

    # dp[j]: j本のマッチを使って作れる最大の数 tuple(桁数d, prevj, lastdig)
    dp = [None for j in range(n + 1)]
    dp[0] = (0, None, None)
    for j in range(1, n + 1):  # もらう
        for use in [2, 3, 4, 5, 6, 7]:
            jp = j - use
            if jp < 0:
                continue
            if dig[use] is None:
                continue
            if dp[jp] is None:
                continue
            d = dp[jp][0] + 1
            tup = (d, jp, dig[use])
            if (dp[j] is None) or (dp[j][0] < d) or (dp[j][0] == d and dp[j][2] < dig[use]):
                dp[j] = tup

    res = []
    j = n
    while True:
        d, jp, i = dp[j]
        if jp is None:
            break
        res.append(str(i))
        j = jp
    assert len(res) == dp[n][0]

    print(("".join(res)))

def __starting_point():
    main()

__starting_point()
