class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        curr = 0
        ans = 0
        seen = set()
        for num in nums:
            seen.add(curr)
            curr += num
            want = curr - target
            if want in seen:
                ans += 1
                seen = set()
                curr = 0
        return ans
