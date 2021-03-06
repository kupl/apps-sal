class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        dp = [[0, 0] for _ in range(n + 2)]
        num = [0] * (n + 2)
        d = defaultdict(int)
        ans = -1
        for i in range(1, n + 1):
            x = arr[i - 1]
            num[x] = 1
            l = dp[x - 1][1]
            r = dp[x + 1][0]
            d[l] -= 1
            d[r] -= 1
            d[dp[x - 1][0]] -= 1
            d[dp[x + 1][1]] -= 1
            dp[x - 1] = [0, 0]
            dp[x + 1] = [0, 0]
            d[0] += 4
            d[dp[x - l][0]] -= 1
            d[dp[x + r][1]] -= 1
            dp[x - l][0] = r + l + 1
            dp[x + r][1] = r + l + 1
            d[r + l + 1] += 2
            if d[m] != 0:
                ans = i
        return ans
