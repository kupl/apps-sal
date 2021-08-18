class Solution:
    def longestSubarray(self, xs: List[int]) -> int:
        n = len(xs)

        if n < 2:
            return 0

        dp = collections.deque()
        best = 0
        for i, x in enumerate(xs):
            if x:
                dp.append(i)
            while dp and i - dp[0] - len(dp) + 1 > 1:
                dp.popleft()
            nholes = i - dp[0] - len(dp) + 1 if dp else 1
            this_len = len(dp) - (not dp[0] and not nholes) if dp else 0
            best = max(best, this_len)

        return best
