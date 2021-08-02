n = int(input())
aa = input()
ab = input()
ba = input()
bb = input()

mod = 10**9 + 7


def solve(n, aa, ab, ba, bb):
    if n <= 3:
        print(1)
        return
    if ab == aa == 'A':
        print(1)
    elif ab == bb == 'B':
        print(1)
    elif ab == 'A' and aa == 'B':
        if ba == 'B':
            print(pow(2, n - 3, mod))
        else:
            # n-3の区間にaaを除く全パターン
            dp = [[0] * 2 for i in range(n + 1)]
            dp[0][0] = 1
            dp[0][1] = 1
            for i in range(n):
                dp[i + 1][0] = (dp[i + 1][0] + dp[i][1]) % mod
                dp[i + 1][1] = (dp[i + 1][1] + dp[i][0] + dp[i][1]) % mod
            ans = (dp[n - 4][0] + dp[n - 4][1]) % mod
            print(ans)
    elif ab == 'B' and bb == 'A':
        if ba == 'A':
            print(pow(2, n - 3, mod))
        else:
            # n-3の区間にaaを除く全パターン
            dp = [[0] * 2 for i in range(n + 1)]
            dp[0][0] = 1
            dp[0][1] = 1
            for i in range(n):
                dp[i + 1][0] = (dp[i + 1][0] + dp[i][1]) % mod
                dp[i + 1][1] = (dp[i + 1][1] + dp[i][0] + dp[i][1]) % mod
            ans = (dp[n - 4][0] + dp[n - 4][1]) % mod
            print(ans)
    else:
        pass
        print('ptn5')


"""
from itertools import product
for n in range(3, 100):
    for bit in product(['A', 'B'], repeat=4):
        aa, ab, ba, bb = bit
        solve(n, aa, ab, ba, bb)
"""
solve(n, aa, ab, ba, bb)
