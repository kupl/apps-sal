class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp, res = collections.deque(), -float('inf')
        for i, n in enumerate(nums):
            if dp and dp[0][0] < i - k:
                dp.popleft()
            cur = n + (0 if not dp else dp[0][1])
            res = max(res, cur)
            if cur > 0:
                while dp and dp[-1][1] <= cur:
                    dp.pop()
                dp.append((i, cur))
        return res
