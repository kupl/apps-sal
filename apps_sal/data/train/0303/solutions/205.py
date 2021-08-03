class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1 for _ in range(n)]

        def max_sum(i):
            # print(i)
            if i >= n:
                return 0
            if i == (n - 1):
                return arr[i]

            if dp[i] != -1:
                return dp[i]

            ans = float('-inf')
            maxi = arr[i]
            for p in range(1, k + 1):
                v = maxi * p + max_sum(i + p)
                # print(i, p, v)
                ans = max(v, ans)
                if (i + p) < n:
                    maxi = max(maxi, arr[i + p])
                else:
                    break
            dp[i] = ans
            return ans

        v = max_sum(0)
        return v
