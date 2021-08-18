class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        cnt = collections.Counter()
        cnt[0] = 0
        ans = 0
        prefix = 0
        for n in nums:
            prefix += n
            if prefix - target in cnt:
                ans += 1
                cnt = collections.Counter()
            cnt[prefix] += 1
        return ans
