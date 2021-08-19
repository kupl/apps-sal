class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        from collections import defaultdict as dd
        n = len(arr)
        cnt = 0
        dp = [[-1] * n for i in range(n)]
        for i in range(n):
            curr = arr[i]
            dp[i][i] = curr
            for j in range(i + 1, n):
                curr = curr ^ arr[j]
                dp[i][j] = curr
        for i in range(1, n):
            map = dd(int)
            for j in range(i):
                map[dp[j][i - 1]] += 1
            for j in range(i, n):
                cnt += map[dp[i][j]]
                if map[dp[i][j]] == 0:
                    del map[dp[i][j]]
        return cnt
