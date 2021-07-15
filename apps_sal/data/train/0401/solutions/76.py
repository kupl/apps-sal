class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        seen = [0, 0, 0]
        for n in nums:
            for s in seen[:]:
                seen[(s + n) % 3] = max(seen[(s + n) % 3], s + n)
        return seen[0]
