class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        tot = sum(nums) % p
        if tot == 0:
            return 0
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        prev = {0: -1}
        best = n
        for i in range(n):
            r = prefix[i] % p
            if (r - tot) % p in prev:
                best = min(best, i - prev[(r - tot) % p])
            prev[r] = i
        if best == n:
            best = -1
        return best
