import sys


class HSubsequencesHardVersion:

    def solve(self):
        (n, k) = [int(_) for _ in input().split()]
        s = input()
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        last = {key: -1 for key in (chr(x) for x in range(ord('a'), ord('z') + 1))}
        for i in range(1, n + 1):
            dp[i][0] = 1
            for j in range(1, i + 1):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] - (dp[last[s[i - 1]]][j - 1] if last[s[i - 1]] != -1 else 0)
            last[s[i - 1]] = i - 1
        ans = 0
        tot = 0
        for sz in range(n, -1, -1):
            ans += min(k - tot, dp[n][sz]) * (n - sz)
            tot = min(k, tot + dp[n][sz])
            if tot == k:
                break
        if tot >= k:
            print(ans)
        else:
            print(-1)


solver = HSubsequencesHardVersion()
input = sys.stdin.readline
solver.solve()
