class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        s = set()
        s.add(0)
        ans = 0
        prefsum = 0
        for num in nums:
            prefsum += num
            if prefsum - target in s:
                ans += 1
                s = set()
            s.add(prefsum)
        return ans
