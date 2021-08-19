class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        seen = [0, 0, 0]
        for n in nums:
            for j in [i + n for i in seen]:
                seen[j % 3] = max(seen[j % 3], j)
        return seen[0]
