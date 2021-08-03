class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        self.dp = [-1 for i in range(n)]

        def helper(pos: int) -> int:
            if pos >= n:
                return 0
            if self.dp[pos] != -1:
                return self.dp[pos]
            current_max = arr[pos]
            ret = arr[pos] + helper(pos + 1)
            for i in range(1, k):
                pos2 = pos + i
                if pos2 >= n:
                    break
                current_max = max(current_max, arr[pos2])
                ret = max(ret, current_max * (i + 1) + helper(pos2 + 1))
            self.dp[pos] = ret
            return ret
        return helper(0)
