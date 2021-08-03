class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        prev = 0
        cnt = 0
        pmax = 0
        for i in range(0, n):
            if nums[i] == 1:
                cnt += 1
            else:
                prev = cnt
                cnt = 0

            maxm = prev + cnt
            if maxm > pmax:
                pmax = maxm

        if cnt == n:
            return (n - 1)
        else:
            return maxm if maxm > pmax else pmax
